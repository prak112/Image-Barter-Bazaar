# Generated by Django 4.1 on 2023-11-14 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_customer_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='customer_type',
            new_name='user_type',
        ),
    ]