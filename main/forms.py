from django.forms import ModelForm
from main.models import FoodEntry
from django.utils.html import strip_tags

class FoodEntryForm(ModelForm):
    class Meta:
        model = FoodEntry
        fields = ["foods", "description", "quantity"]


    def clean_mood(self):
        foods = self.cleaned_data["foods"]
        return strip_tags(foods)

    def clean_feelings(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)