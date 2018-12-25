from django import forms
from .models import UserInputValues
from django.contrib.admin import widgets                                       

class NewUserInputForm(forms.ModelForm):
	# Time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
	class Meta:
		model = UserInputValues
		fields = ['Location','Kind_of_info','Criticality']