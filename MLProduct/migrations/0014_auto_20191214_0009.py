# Generated by Django 3.0 on 2019-12-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLProduct', '0013_auto_20191213_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients_models',
            old_name='client_joining_date',
            new_name='client_opening_date',
        ),
        migrations.AlterField(
            model_name='clients_models',
            name='client_annual_income',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='clients_models',
            name='client_annual_income_slab',
            field=models.CharField(blank=True, choices=[('', 'Choose...'), ('1', '1 - <= 1 Lakh'), ('2', '> 1 Lakh - <= 2.5 Lakh'), ('3', '> 2.5 Lakh - <= 5 Lakh'), ('4', 'Above 5 Lakh')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients_models',
            name='client_annual_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
