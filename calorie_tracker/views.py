from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm
from django.views.decorators.http import require_POST

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

@require_POST
def delete_item(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('tracker')

@require_POST
def reset_items(request):
    FoodItem.objects.all().delete()
    return redirect('tracker')
