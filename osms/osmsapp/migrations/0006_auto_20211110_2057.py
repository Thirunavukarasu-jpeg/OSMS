# Generated by Django 3.2.5 on 2021-11-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmsapp', '0005_auto_20211110_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitaldetail',
            name='total_doctors',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='hospitaldetail',
            name='total_nurses',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]