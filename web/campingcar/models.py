from django.db import models
import os
from web.settings import MEDIA_ROOT

OPTION_DICT = {"AirConditioner" : "냉난방", "DoorAndWindow" : "도어 & 창문", 
					  "Earning" : "어닝", "Battery" : "배터리",
					  "Charger" : "AC 충전기", "Inverter" : "인버터", 
					  "SolarPanel" : "태양광시스템", "ETC": "기타"}

class Car(models.Model):
	MODEL_CHOICES = (("TruckCamper", "트럭캠퍼"), ("TruckBase", "트럭베이스"), 
					  ("VanBase", "밴베이스"), ("SpecificPurpose", "특수목적"), 
					  ("Trailer", "트레일러"))
	name = models.CharField(max_length=100)
	type = models.CharField(max_length = 100,
								   choices = MODEL_CHOICES,
								   null = False,
								   blank = False,
								   default = MODEL_CHOICES[0][0])
	explanation = models.TextField(default="차량 설명을 입력하세요.")
	image = models.ImageField(upload_to = 'images/car', blank = True, null = True)
	price = models.IntegerField(default=0)

	def __str__(self):
		return self.name


class Option(models.Model):
	OPTION_CHOICES = (("AirConditioner", "냉난방"), ("DoorAndWindow", "도어 & 창문"), 
					  ("Earning", "어닝"), ("Battery", "배터리"), 
					  ("Charger", "AC 충전기"), ("Inverter", "인버터"), 
					  ("SolarPanel", "태양광시스템"), ("ETC", "기타"))
	
	name = models.CharField(max_length=100)
	explanation = models.CharField(max_length=100,
								   null = True,
								   blank = True)

	car = models.ManyToManyField(Car, blank=True)

	type = models.CharField(max_length = 100,
								   choices = OPTION_CHOICES,
								   null = False,
								   blank = False,
								   default = OPTION_CHOICES[-1][0])
	image = models.ImageField(upload_to = 'images/options', blank = True, null = True)
	price = models.IntegerField()

	def __str__(self):
		return self.name  + ", " + str(self.price)  + "원"

