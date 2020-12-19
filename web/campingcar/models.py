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
	name = models.CharField(max_length=100,
							help_text='차량의 이름을 입력하세요')

	type = models.CharField(max_length = 100,
								   choices = MODEL_CHOICES,
								   null = False,
								   blank = False,
								   default = MODEL_CHOICES[0][0],
								   help_text='차량의 종류를 선택하세요')
	explanation = models.TextField(default="",
								   help_text='차량의 설명을 입력하세요')
	image = models.ImageField(upload_to = 'images/car', 
							  blank = True, null = True,
							  help_text='차량의 이미지를 업로드하세요')
	price = models.IntegerField(default=0,
							    help_text='차량의 가격을 입력하세요')

	contract_payment = models.IntegerField(default=25,
							    help_text='계약금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!')
	advanced_payment_1 = models.IntegerField(default=25,
							    help_text='1차 중도금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!')
	advanced_payment_2 = models.IntegerField(default=25,
							    help_text='2차 중도금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!')
	remaining_payment = models.IntegerField(default=25,
							    help_text='잔금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!')

	def __str__(self):
		return self.name


class Option(models.Model):
	OPTION_CHOICES = (("AirConditioner", "냉난방"), ("DoorAndWindow", "도어 & 창문"), 
					  ("Earning", "어닝"), ("Battery", "배터리"), 
					  ("Charger", "AC 충전기"), ("Inverter", "인버터"), 
					  ("SolarPanel", "태양광시스템"), ("ETC", "기타"))
	
	name = models.CharField(max_length=100,
							help_text='옵션의 이름을 입력하세요')
	explanation = models.CharField(max_length=100,
								   null = True,
								   blank = True,
								   help_text='옵션의 설명을 입력하세요')

	car = models.ManyToManyField(Car, blank=True,
								 help_text='옵션이 적용가능한 차량들을 선택하세요. ')

	type = models.CharField(max_length = 100,
								   choices = OPTION_CHOICES,
								   null = False,
								   blank = False,
								   default = OPTION_CHOICES[-1][0],
								   help_text='옵션의 종류를 선택하세요')
	image = models.ImageField(upload_to = 'images/options', 
							  blank = True, null = True,
							  help_text='옵션의 이미지를 업로드하세요')
	price = models.IntegerField(default=0,
		 						help_text='옵션의 가격을 입력하세요')

	def __str__(self):
		return self.name  + ", " + str(self.price)  + "원"

class Company(models.Model):
	name = models.CharField(max_length=100,
							help_text='제작사의 상호명을 입력하세요')
	business_number = models.CharField(max_length=100,
									   help_text='제작사의 사업자번호를 입력하세요')
	address = models.CharField(max_length=200,
							   help_text='제작사의 주소를 입력하세요')
	ceo_name = models.CharField(max_length=100,
								help_text='제작사의 대표자명을 입력하세요')
	car = models.ManyToManyField(Car, blank=True,
								 help_text='제작사가 만드는 차량들을 선택하세요. ')
	
	def __str__(self):
		return self.name + "(대표: " + self.ceo_name + ")"
