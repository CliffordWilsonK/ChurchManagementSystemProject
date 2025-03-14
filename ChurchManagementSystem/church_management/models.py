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
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class ChurchMember(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    MARITAL_STATUS = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ]
    FELLOWSHIPS = [
        ('children', 'Children Ministry'),
        ('junior_youth', 'Junior Youth'),
        ('youth', 'Youth Fellowship'),
        ('women', 'Women\'s Fellowship'),
        ('men', 'Men\'s Fellowship'),
        ('gospel', 'Gospel Band')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email= models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=GENDER)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)
    occupation = models.CharField(max_length=100)
    fellowship = models.CharField(max_length=100, choices=FELLOWSHIPS)
    join_date = models.DateField(auto_now_add=True)
