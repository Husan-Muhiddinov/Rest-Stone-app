# Generated by Django 4.1.7 on 2023-03-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cost',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
