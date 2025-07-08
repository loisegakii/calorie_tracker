from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm

def calorie_tracker(request):
    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker')
    else:
        form = FoodItemForm()

    return render(request, 'calorie_tracker/tracker.html', {
        'form': form,
        'food_items': food_items,
        'total_calories': total_calories,
    })
