# Generated by Django 3.0.6 on 2020-06-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200621_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
