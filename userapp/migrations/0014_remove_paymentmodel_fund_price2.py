# Generated by Django 4.0.3 on 2022-04-08 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_rename_fund_price_paymentmodel_fund_price2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='fund_price2',
        ),
    ]
