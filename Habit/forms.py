from django import forms
from .models import Habit

class AddForm(forms.ModelForm):
	class Meta:
		model=Habit
		fields=["habit","Mon","Tue","Wed","Thu","Fri","Sat","Sun","Time"]