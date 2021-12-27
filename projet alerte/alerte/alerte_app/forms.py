from django.forms import ModelForm
from .models import alerte
from django.db import models
from django.db.models import fields
from .forms import alerteForm

class alerteForm(ModelForm):
						class Meta:
							model = alerte
							fields = ( 'Nom', 'Prenom', 'Localisation', 'Heure', 'Description', 'Commissariat' , )

							labels = {
								'heure': '',  
								'description': '',    
								'user': '',  
								'localisation': '', 
								'police_centrale': '',
	
							}

							widgets = {
								'heure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'heure',}),  
								'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description',}), 
								'user': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user',}), 
								'localisation': forms.Select(attrs={'class': 'form-select', 'placeholder': 'localisation',}),  
								'police_centrale': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'police_centrale',}),   
							}