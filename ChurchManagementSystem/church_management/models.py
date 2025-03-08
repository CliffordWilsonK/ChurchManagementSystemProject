from django.db import models

# Create your models here.
class Financial_Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('tithe', 'Tithe'),
        ('offering', 'Offering'),
        ('seed', 'Seed'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)


class ChurchProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class ChurchMember(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    join_date = models.DateField(auto_now_add=True)
