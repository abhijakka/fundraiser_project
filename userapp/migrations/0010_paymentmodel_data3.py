# Generated by Django 4.0.3 on 2022-04-07 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_paymentmodel_submitted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='data3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.fundraisermodel'),
        ),
    ]