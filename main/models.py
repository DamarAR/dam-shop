from django.contrib.auth.models import User
from django.db import models
import uuid  

# Create your models here.
class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    foods = models.CharField(max_length=250)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    quantity = models.IntegerField()
    