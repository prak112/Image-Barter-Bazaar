# Generated by Django 4.1 on 2023-11-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0012_alter_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(default='https://www.pexels.com/', verbose_name='Source'),
        ),
    ]
