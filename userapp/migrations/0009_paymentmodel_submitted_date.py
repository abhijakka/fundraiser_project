# Generated by Django 4.0.3 on 2022-04-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_fundraisermodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='submitted_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
