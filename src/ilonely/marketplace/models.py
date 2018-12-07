from django.db import models
from pages.models import Profile

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, blank=False)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="product_pictures/", default="product_pictures/no-image-available.png", null=True, blank=True)
    location = models.CharField(max_length=150, blank=True, default='')
    sold = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, default='', max_length=450)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    offer = models.PositiveIntegerField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return "%s wants to buy %s" % (self.buyer.user.get_username(), self.product.name)
