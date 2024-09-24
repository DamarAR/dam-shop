from django.contrib.auth.models import User
from django.db import models
import uuid  

# Create your models here.
class FoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    time = models.DateField(auto_now_add=True)
    foods = models.CharField(max_length=250)
    description = models.TextField()
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)