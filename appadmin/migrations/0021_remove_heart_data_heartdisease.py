# Generated by Django 4.1.7 on 2023-07-12 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0020_alter_heart_data_chestpaintype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heart_data',
            name='HeartDisease',
        ),
    ]
