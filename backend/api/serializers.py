from rest_framework import serializers
from api.models import User, Catering, VariantCaterings, Order
from django.db import transaction
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username',
                  'id',
                  'role')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password', None)
        return representation

        
class VariantCateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantCaterings
        fields = (
            'id',
            'variant_name',
            'extra_price',
        )

class CateringSerializer(serializers.ModelSerializer):
    catering_variants = VariantCateringSerializer(many=True)
    class Meta:
        model = Catering
        fields = (
            'id',
            'title',
            'imageLink',
            'price',
            'created_by',
            'catering_variants',
            'is_closed',
            'quantity'
            'created_at',
        )
    
    def create(self, validated_data):
        variants = validated_data.pop('catering_variants')
        catering = Catering.objects.create(**validated_data)
        for variant in variants :
            VariantCaterings.objects.create(catering=catering, **variant)
        return catering


class OrderCateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = (
            'id',
            'title',
            'price',
            'imageLink'
        )

class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'role'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'ordered_by',
            'ordered_at',
            'is_paid',
            'catering',
            'notes',
            'variant'
        )
        extra_kwargs = {
            'variant': {'required': False, 'allow_null': True},
        }


class OrderCateringViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = (
            'title',
            'price'
        )

class OrderViewSerializer(serializers.ModelSerializer):
    ordered_by = OrderUserSerializer()
    variant = VariantCateringSerializer()
    catering = OrderCateringViewSerializer()
    class Meta:
        model = Order
        fields = (
            'id',
            'ordered_by',
            'ordered_at',
            'is_paid',
            'catering',
            'notes',
            'variant'
        )
        extra_kwargs = {
            'variant': {'required': False, 'allow_null': True},
        }


class CateringViewSerializer(serializers.ModelSerializer):
    order =  OrderViewSerializer(source='catering', many=True)
    catering_variants = VariantCateringSerializer(many=True)
    class Meta:
        model = Catering
        fields = (
            'id',
            'title',
            'price',
            'created_at',
            'created_by',
            'catering_variants',
            'is_closed',
            'quantity',
            'order'
        )