# Generated by Django 5.0.7 on 2024-10-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]