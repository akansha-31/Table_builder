from django.db import models
from . import User

class TableRecords(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=20)
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField()