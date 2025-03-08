from django.db import models

# Create your models here.
class Financial_Transactions(models.Model):
    CATEGORY_CHOICES = [
        ('tithe', 'Tithe'),
        ('offering', 'Offering'),
        ('seed', 'Seed'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

