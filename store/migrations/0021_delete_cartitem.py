# Generated by Django 5.0.7 on 2024-10-28 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_cartitem_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]