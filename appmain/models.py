from django.db import models

# Create your models here.
# class adminuser(models.Model):
#     main_id = models.AutoField(primary_key=True)
#     Full_name= models.CharField(max_length=100,null=True)
#     Image= models.FileField(upload_to='Images/user')
#     Email= models.EmailField(max_length=50,null=True)
#     Address= models.CharField(max_length=150,null=True)
#     Age= models.IntegerField(null=True)
#     Phone=models.IntegerField(null=True)
#     Password=models.CharField(max_length=30,null=True)
#     class Meta:
#         db_table = 'admin_details'