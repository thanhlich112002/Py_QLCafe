# Generated by Django 4.1.7 on 2023-04-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_remove_cart_type_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]