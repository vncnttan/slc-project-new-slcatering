from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True) # ex. NJ23-1 / Nama Toko
    role = models.CharField(max_length=50, blank=False, default="user")  # customer / merchant
    access_token = models.CharField(max_length=255, blank=True) # JWT Token generated, not from Messier

class Catering(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=200, blank=False)
    imageLink = models.CharField(max_length=255, blank=False)
    price = models.IntegerField(blank=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='caterings')
    is_closed = models.BooleanField(default=False, blank=False)
    quantity = models.IntegerField(default=0, blank=False) # maksudnya stock barang
    created_at = models.DateTimeField(blank=False)

class VariantCaterings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    variant_name = models.CharField(max_length=255, blank=False)
    extra_price = models.IntegerField(blank=False)
    catering = models.ForeignKey(to=Catering, on_delete=models.CASCADE, related_name='catering_variants')

class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable = False, primary_key=True)
    ordered_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='ordered_by')
    ordered_at = models.DateTimeField(blank=False)
    is_paid = models.BooleanField(default=False, blank=False)
    notes = models.CharField(max_length=255, blank=False)
    variant = models.ForeignKey(to = VariantCaterings, on_delete=models.CASCADE, related_name="variant", null=True, blank=True)
    catering = models.ForeignKey(to = Catering, on_delete=models.CASCADE, related_name="catering")
    
    