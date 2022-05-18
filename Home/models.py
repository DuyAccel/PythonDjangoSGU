from django.db import models
from Account.models import User

class Product (models.Model):
    id = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100, verbose_name='Tên SP')
    ProductStar = models.IntegerField(verbose_name='Sao SP')
    ProductBrand = models.CharField(max_length=100, verbose_name='Hãng SP')
    ProductNumber = models.IntegerField(verbose_name='S.Lượng SP')
    ProductNewPrice = models.IntegerField(verbose_name='Giá mới SP')
    ProductOldPrice = models.IntegerField(verbose_name='Giá cũ SP')
    ProductImage1 = models.CharField(max_length=1000, verbose_name='Ảnh SP 1')
    ProductImage2 = models.CharField(max_length=1000, verbose_name='Ảnh SP 2')
    ProductImage3 = models.CharField(max_length=1000, verbose_name='Ảnh SP 3')
    ProductRam = models.IntegerField(verbose_name='Ram')
    ProductRom = models.IntegerField(verbose_name='Rom')
    def __str__(self):
        return self.ProductName 

class Cart(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey('Account.User', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    amount = models.IntegerField()
