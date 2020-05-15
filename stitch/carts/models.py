from django.db import models
from store.models import Product


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product.productName


class Cart(models.Model):
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} | $Total: {}".format(self.id, self.total)
