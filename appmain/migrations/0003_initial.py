# Generated by Django 4.1.6 on 2023-03-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appmain', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('main_id', models.AutoField(primary_key=True, serialize=False)),
                ('Full_name', models.CharField(max_length=100, null=True)),
                ('Image', models.FileField(upload_to='Images/user')),
                ('Email', models.EmailField(max_length=50, null=True)),
                ('Address', models.CharField(max_length=150, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('Password', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'admin_details',
            },
        ),
    ]