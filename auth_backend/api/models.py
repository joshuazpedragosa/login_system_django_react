from django.db import models

# Create your models here.
class user_credentials(models.Model):
    name = models.CharField(max_length=100, null=False, default='')
    email = models.CharField(max_length=100, null=False, default='')
    phone_num = models.IntegerField(default=0, null=False)
    password = models.CharField(max_length=100, null=False, default='')
    
    class Meta:
        db_table = 'tbl_credentials'