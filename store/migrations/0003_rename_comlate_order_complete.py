# Generated by Django 3.2.10 on 2022-07-13 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='comlate',
            new_name='complete',
        ),
    ]
