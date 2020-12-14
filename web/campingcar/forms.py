from django import forms

class EstimateForm(forms.Form):
	def __init__(self, *args, **kwargs):
		print("Hello, World!")
		print(args)