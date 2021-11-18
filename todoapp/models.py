from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Costlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  added_date = models.DateTimeField()
  text = models.CharField(max_length = 200)
  amount = models.FloatField()
  person_used = models.CharField(max_length=30, default="dont know")

  def __str__(self):
      return f"COSTobjOf_{self.user}"