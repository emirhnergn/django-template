from django.db import models

class DateAbstarctModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True