from django.db import models

# Create your models here.
class Items(models.Model):
    nama = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    jumlah = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)