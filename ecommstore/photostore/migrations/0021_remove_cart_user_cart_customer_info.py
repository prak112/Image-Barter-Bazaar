# Generated by Django 4.1 on 2023-12-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0020_cart_user_alter_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='customer_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='potential_customers', to='photostore.customer'),
        ),
    ]
