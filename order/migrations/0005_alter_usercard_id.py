# Generated by Django 5.0.7 on 2024-10-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_usercard_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]