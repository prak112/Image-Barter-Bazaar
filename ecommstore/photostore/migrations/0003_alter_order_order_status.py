# Generated by Django 4.1 on 2023-12-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('SHIP', 'Delivered by Post'), ('DEL', 'Delivered by Email')], max_length=30, verbose_name='Order Status'),
        ),
    ]
