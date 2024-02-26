from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    statuses = [
        ('D', 'Delivery'),
        ('ND', 'Not Delivery')
    ]
    status = models.CharField(max_length=2, choices=statuses)
    payments = [
        ('Card', 'Card'),
        ('Cash', 'Cash')
    ]
    payment = models.CharField(max_length=4, choices=payments)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product ID: {self.pk}'
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='items')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table= 'order_items'