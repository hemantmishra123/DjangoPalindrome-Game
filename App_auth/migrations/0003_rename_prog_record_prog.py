# Generated by Django 3.2.4 on 2022-10-29 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_auth', '0002_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='prog',
            new_name='Prog',
        ),
    ]