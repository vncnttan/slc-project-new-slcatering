from api.serializers import OrderSerializer
from api.models import Order, Catering
from datetime import datetime
from django.http.response import JsonResponse
from rest_framework import status
from api.models import User, Order
from django.db import transaction
from django.db.models import Sum, F


@transaction.atomic
def create_order(user_id, order):
    try:
        if 'username' in order and 'password' in order:
            order.pop('username')
            order.pop('password')
            
        #check if user have any unpaid in history
        debt = get_user_unpaid(user_id)
        if debt >= 50000:
            return JsonResponse({"message": f"You have debt of Rp.{debt},00 Please finish your payment before ordering more catering"}, status=status.HTTP_402_PAYMENT_REQUIRED)
        
        #check if the quantity is < then all the quantity order
        
        catering_details = Catering.objects.select_for_update().get(id = order['catering'])
        all_order = Order.objects.filter(catering=order['catering']).count()
        
        if all_order < catering_details.quantity:
            order['ordered_by'] = user_id
            order['ordered_at'] = datetime.now()
            order['is_paid'] = False
            # print(order)
            new_order = OrderSerializer(data=order)
            if new_order.is_valid():
                new_order.save()
                return JsonResponse(new_order.data, status=status.HTTP_200_OK)
            else :
                return JsonResponse({"message" : "Not succesfull", "error":new_order.errors}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message" : "Out of stock"}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e :
        return JsonResponse({"message":"Server error", "error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def get_user_unpaid (user_id):
    orders = Order.objects.filter(ordered_by = user_id, is_paid = False)
    total = 0
    # print(len(orders))
    for order in orders:
        item_total = 0
        if order.variant != None:
            item_total += order.variant.extra_price
        item_total += order.catering.price
        total += item_total
        # print(total)
    
    return total