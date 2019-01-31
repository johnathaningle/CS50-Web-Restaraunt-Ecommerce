from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from .serializers import FoodSerializer
from rest_framework import viewsets

def index(request):
    food_objects = Food.objects.all()
    foods = []
    for food in food_objects:
        item = {}
        item["Category"] = str(food.category)
        item["Name"] = str(food.name)
        item["Toppings"] = str(food.toppings)
        item["Size"] = str(food.size)
        item["Price"] = float(food.price)
        foods.append(item)
    food_data = {}
    for food in foods:
        category = food["Category"]
        food_attrs = {"name":[food['Name']], "toppings":[food['Toppings']], "size":[food['Size']], "price":[food['Price']]}
        try:
            if food['Name'] not in list(food_data[category][0]["name"]):
                food_data[category][0]["name"].append(food['Name'])
            if food['Toppings'] not in list(food_data[category][0]["toppings"]):
                food_data[category][0]["toppings"].append(food['Toppings'])
            if food['Size'] not in list(food_data[category][0]["size"]):
                food_data[category][0]["size"].append(food['Size'])
            food_data[category][0]["price"].append(food['Price'])
        except KeyError:
            food_data[category] = []
            food_data[category].append(food_attrs)
    context = {
        "foods": food_data
    }
    return render(request, 'home/index.html', context=context)

def about(request):
    return render(request, 'home/about.html')

# class FoodViewSet(viewsets.ModelViewSet):
#     queryset = Food.objects.