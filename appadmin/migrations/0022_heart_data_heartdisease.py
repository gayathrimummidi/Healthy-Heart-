# Generated by Django 4.1.7 on 2023-07-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0021_remove_heart_data_heartdisease'),
    ]

    operations = [
        migrations.AddField(
            model_name='heart_data',
            name='HeartDisease',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
