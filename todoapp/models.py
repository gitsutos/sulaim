from django.db import models

# Create your models here.
class Todo(models.Model):
  added_date = models.DateTimeField()
  text = models.CharField(max_length = 200)
  amount = models.FloatField()
  person_used = models.CharField(max_length=30, default="dont know")