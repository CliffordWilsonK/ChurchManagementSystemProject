# Generated by Django 5.1.6 on 2025-03-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_management', '0008_alter_churchproject_collected_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchmember',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
