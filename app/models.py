from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
 
 
class User(AbstractUser):
   pass
 
class TableRecords(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=20)
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField()

class TableColumns(models.Model):
   c_id = models.AutoField(primary_key=True)
   column_name = models.CharField(max_length=20)
   column_type = models.CharField(max_length=20)
   is_primary = models.BooleanField()
   nullable = models.BooleanField(default=False)
   t_id = models.ForeignKey(TableRecords, on_delete=models.CASCADE, null=True)

