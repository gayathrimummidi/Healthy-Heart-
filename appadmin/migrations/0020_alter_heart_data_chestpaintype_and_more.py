# Generated by Django 4.1.7 on 2023-07-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0019_alter_heart_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heart_data',
            name='ChestPainType',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heart_data',
            name='ExerciseAngina',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heart_data',
            name='RestingECG',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heart_data',
            name='ST_Slope',
            field=models.IntegerField(max_length=100),
        ),
    ]
