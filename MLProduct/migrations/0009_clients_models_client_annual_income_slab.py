# Generated by Django 3.0 on 2019-12-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLProduct', '0008_auto_20191212_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients_models',
            name='client_annual_income_slab',
            field=models.CharField(choices=[('', 'Choose...'), ('1', '1 - <= 1 Lakh'), ('2', '> 1 Lakh - <= 2.5 Lakh'), ('3', '> 2.5 Lakh - <= 5 Lakh'), ('4', 'Above 5 Lakh')], default='', max_length=20),
        ),
    ]
