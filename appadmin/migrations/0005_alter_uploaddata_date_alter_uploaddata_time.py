# Generated by Django 4.1.7 on 2023-03-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0004_alter_uploaddata_date_alter_uploaddata_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddata',
            name='Date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='uploaddata',
            name='Time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
