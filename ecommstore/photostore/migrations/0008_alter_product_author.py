# Generated by Django 4.1 on 2023-11-10 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0007_remove_product_item_url_remove_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author_fullname', to='photostore.customer', to_field='fullname'),
        ),
    ]