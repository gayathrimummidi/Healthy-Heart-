# Generated by Django 4.1.6 on 2023-03-13 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0006_alter_uploaddata_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploaddata',
            old_name='Image',
            new_name='File',
        ),
    ]
