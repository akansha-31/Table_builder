from django.db import models
from . import TableRecords

CHOICES = [
    ('String', 'String'),
    ('Boolean', 'Boolean'),
    ('Number', 'Number'),
    ('Email', 'Email'),
    ('DateTime', 'DateTime')
]

class TableColumns(models.Model):
   c_id = models.AutoField(primary_key=True)
   column_name = models.CharField(max_length=20)
   column_type = models.CharField(CHOICES, max_length=20)
   is_primary = models.BooleanField()
   nullable = models.BooleanField(default=False)
   t_id = models.ForeignKey(TableRecords, on_delete=models.CASCADE, null=True)

