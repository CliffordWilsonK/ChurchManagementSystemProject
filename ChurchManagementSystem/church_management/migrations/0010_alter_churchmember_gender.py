# Generated by Django 5.1.6 on 2025-03-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_management', '0009_alter_churchmember_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100),
        ),
    ]
