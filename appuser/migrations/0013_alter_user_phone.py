# Generated by Django 4.1.6 on 2023-03-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0012_rename_profile_pic_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Phone',
            field=models.IntegerField(),
        ),
    ]
