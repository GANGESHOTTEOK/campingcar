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
		option_dict = {}
		option_dict['car'] = car
		for option in option_dict.keys():
			if 'csrf' not in option:
				option_dict[option] = request.POST[option]
		for item in option_dict.keys():
			print("%s, %s"%(item, option_dict[item]))

	return render(request, 'campingcar/estimate.html', {'car' : car})
