# Generated by Django 4.0.3 on 2022-04-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0017_alter_paymentmodel_fund_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='cvv',
            field=models.CharField(help_text='cvv', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='expiarydate',
            field=models.CharField(help_text='expirydate', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='password',
            field=models.CharField(help_text='password', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='selectbank',
            field=models.CharField(help_text='selectbank', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='startmonth',
            field=models.CharField(help_text='start', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='submitted_date2',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='username',
            field=models.CharField(help_text='username', max_length=50, null=True),
        ),
    ]
