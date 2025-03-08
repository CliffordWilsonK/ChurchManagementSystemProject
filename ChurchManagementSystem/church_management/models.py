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


class ChurchProjects(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)