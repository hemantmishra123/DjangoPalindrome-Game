# Generated by Django 3.2.4 on 2022-10-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.IntegerField(max_length=10)),
                ('Ds', models.IntegerField(max_length=10)),
                ('Coa', models.IntegerField(max_length=10)),
                ('Cn', models.IntegerField(max_length=10)),
                ('prog', models.IntegerField(max_length=10)),
            ],
        ),
    ]