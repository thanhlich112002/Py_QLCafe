# Generated by Django 4.1.7 on 2023-05-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_alter_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(blank=True, default='../Manage/static/img/avata.jpg', null=True, upload_to='images/'),
        ),
    ]
