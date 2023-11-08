# Generated by Django 4.1 on 2023-11-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_customer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='customer_type',
            field=models.CharField(choices=[('Artist', 'Art'), ('Photographer', 'Photography'), ('Enthusiast', 'Curiosity')], max_length=20, verbose_name='Interested in ?'),
        ),
    ]