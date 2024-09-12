from django.db import models
import uuid  

# Create your models here.
class FoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # add this line
    foods = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    quantity = models.IntegerField()