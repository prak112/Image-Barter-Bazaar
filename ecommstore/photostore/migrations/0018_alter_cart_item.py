# Generated by Django 4.1 on 2023-12-04 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0017_alter_cart_item_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipped_products', to='photostore.product'),
        ),
    ]
