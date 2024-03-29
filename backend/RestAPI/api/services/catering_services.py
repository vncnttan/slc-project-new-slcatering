from api.models import Catering, VariantCaterings
from api.serializers import CateringSerializer,VariantCateringSerializer, CateringViewSerializer

def get_active_caterings():
    try:
        caterings = Catering.objects.filter(is_closed=False)
        caterings_serializer = CateringViewSerializer(caterings, many=True)
        return caterings_serializer
    except Catering.DoesNotExist:
        return None


def get_all_catering_history():
    try:
        caterings = Catering.objects.filter(is_closed=True)
        caterings_serializer = CateringViewSerializer(caterings, many=True)
        return caterings_serializer
    except Catering.DoesNotExist:
        return None
        

def get_all_caterings():
    try:
        caterings = Catering.objects.all()
        caterings_serializer = CateringViewSerializer(caterings, many=True)
        return caterings_serializer
    except Catering.DoesNotExist:
        return None

def get_all_active_sellers_caterings(id):
    try:
        caterings = Catering.objects.filter(created_by_id=id, is_closed=False)
        caterings_serializer = CateringViewSerializer(caterings, many=True)
        return caterings_serializer
    except Catering.DoesNotExist:
        return None
    
def get_all_past_sellers_caterings(id):
    try:
        caterings = Catering.objects.filter(created_by_id=id, is_closed=True)
        caterings_serializer = CateringViewSerializer(caterings, many=True)
        return caterings_serializer
    except Catering.DoesNotExist:
        return None