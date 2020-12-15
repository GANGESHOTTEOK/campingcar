from django.shortcuts import render, redirect
from .models import Car, Option, OPTION_DICT

class Contract:
	contract_price = 0
	semi_price_1 = 0
	semi_price_2 = 0
	remaining_price = 0

	total_price = 0
	total_price_with_vat = 0
	comsumption_tax = 0
	education_tax = 0
	supply_price = 0
	vat = 0
	registration_tax = 0
	total_tax = 0

	def calcuate(self):
		self.contract_price = self.remaining_price = int(self.total_price * 0.2)
		self.semi_price_1 = self.semi_price_2 = int(self.total_price * 0.3)

		self.comsumption_tax = int(self.total_price * 0.05)
		self.education_tax = int(self.comsumption_tax * 0.3)
		self.vat = int(self.total_price * 0.1)

		self.supply_price = int(self.total_price + self.comsumption_tax + self.education_tax)
		self.registration_tax = int(self.supply_price * 0.05)
		self.total_tax = int(self.comsumption_tax + self.education_tax + self.vat)


def main(request, carType = 0):
	carList = Car.objects.all()
	if carType != 0:
		carList = Car.objects.filter(type = carType)
	return render(request, 'campingcar/index.html', {'carList' : carList})

def estimate(request, name = 0):
	car = Car.objects.get(name = name)

	contract = Contract()
	contract.total_price += car.price

	if request.method == "POST":
		option_dict = {}
		for option in request.POST.keys():
			if 'csrf' not in option:
				option_dict[Option.objects.get(id=option)] = request.POST[option]
				contract.total_price += Option.objects.get(id=option).price * int(request.POST[option])
		
		contract.calcuate()
		return render(request, 'campingcar/detail_estimate.html', 
				     {'car' : car, 'option_dict' : option_dict, 
				      'OPTION_DICT' : OPTION_DICT,
				      'contract' : contract})

	return render(request, 'campingcar/estimate.html', {'car' : car})
