# Generated by Django 4.1 on 2023-12-07 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0024_remove_order_barter_exchange_order_payment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]