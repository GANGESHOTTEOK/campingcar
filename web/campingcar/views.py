from django.shortcuts import render, redirect
from .models import Car


def main(request, carType = 0):
	carList = Car.objects.all()
	if carType != 0:
		carList = Car.objects.filter(type = carType)
	return render(request, 'campingcar/index.html', {'carList' : carList})

def detail(request):
	return render(request, 'campingcar/detail_estimate.html')

def estimate(request, name = 0):
	car = Car.objects.get(name = name)
	if request.method == "POST":
		option_dict = request.POST
	return render(request, 'campingcar/estimate.html', {'car' : car})
