# Generated by Django 5.0.6 on 2024-08-18 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='balance',
            new_name='deposited_balance',
        ),
    ]
