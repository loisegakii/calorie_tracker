from django.db import models
from django.utils import timezone

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.calories} cal"
