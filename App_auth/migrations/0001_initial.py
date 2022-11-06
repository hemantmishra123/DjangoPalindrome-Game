# Generated by Django 3.2.4 on 2022-10-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Roll_No', models.IntegerField(max_length=10)),
                ('Father', models.CharField(max_length=50)),
                ('Mother', models.CharField(max_length=50)),
                ('Math', models.IntegerField(max_length=50)),
                ('English', models.IntegerField(max_length=50)),
                ('Physics', models.IntegerField(max_length=50)),
            ],
        ),
    ]
