from django.forms import ModelForm 
from .models import Room 

class RoomForm(ModelForm):
	class Meta:
		model = Room 
		fields = '__all__'     #gonna create form based on all the attributes from Room class