from django.shortcuts import render, redirect
from .models import Car, Option, OPTION_DICT

def main(request, carType = 0):
	carList = Car.objects.all()
	if carType != 0:
		carList = Car.objects.filter(type = carType)
	return render(request, 'campingcar/index.html', {'carList' : carList})

def estimate(request, name = 0):
	car = Car.objects.get(name = name)
	if request.method == "POST":
		option_dict = {}
		for option in request.POST.keys():
			if 'csrf' not in option:
				option_dict[Option.objects.get(id=option)] = int(request.POST[option])
		return render(request, 'campingcar/detail_estimate.html', 
				     {'car' : car, 'option_dict' : option_dict, "OPTION_DICT" : OPTION_DICT})

	return render(request, 'campingcar/estimate.html', {'car' : car})
