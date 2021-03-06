from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Dates:
  date = models.DateField(auto_now_add=True)
  time = models.TimeField

class Costlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  added_date = models.DateTimeField(auto_now_add=True)
  text = models.CharField(max_length = 200)
  amount = models.FloatField()
  person_used = models.CharField(max_length=30, default="dont know")

  def serialize(self):
    return {
      "date":self.added_date,
      "amount":self.amount,
      "description":self.text,
      "person_used":self.person_used,
      "id":self.id
    }

  def __str__(self):
      return f"COSTobjOf_{self.user}"