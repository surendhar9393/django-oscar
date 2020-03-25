# Generated by Django 2.1.1 on 2020-03-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_auto_20200130_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/products/%Y/%m/', verbose_name='Original'),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='delivery_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Delivery Charge'),
        ),
    ]
