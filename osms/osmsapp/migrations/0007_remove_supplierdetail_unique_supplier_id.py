# Generated by Django 3.2.5 on 2021-11-11 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osmsapp', '0006_auto_20211110_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierdetail',
            name='unique_supplier_id',
        ),
    ]
