# Generated by Django 4.0.3 on 2022-04-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='name',
            field=models.CharField(help_text='Enter Your Name', max_length=100, null=True),
        ),
    ]
