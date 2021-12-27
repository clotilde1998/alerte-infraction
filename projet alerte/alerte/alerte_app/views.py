from django.shortcuts import render, redirect
from .models import user
from .models import localisation
from .models import police_centrale
from .models import alerte
from django.http import HttpResponseRedirect
#from .forms import alerteForm
# Create your views here.
def home(request):
	return render(request, 'alertes/home.html', {})



def listeuser(request):
	Users = user.objects.all().order_by('nom')
	return render(request, 'alertes/listeuser.html', {
	'Users': Users,
})

def localisationlist(request):
	Localisations = localisation.objects.all().order_by('adresse')
	return render(request, 'alertes/localisationlist.html', {
	'Localisations': Localisations,
})
def policelist(request):
	Polices = police_centrale.objects.all().order_by('adresse')
	return render(request, 'alertes/policelist.html',{
	'Polices': Polices,
})
def alertelist(request):
	Alertees = alerte.objects.all().order_by('heure')
	return render(request, 'alertes/alertelist.html',{
	'Alertees': Alertees,
})
def nouvelle_alerte(request):
							submitted = False
							if request.method == "POST":
								form = alerteForm(request.POST)
								if form.is_valid():
									form.save()
									return HttpResponseRedirect('/nouvelle_alerte?submitted=True')
							else:
								form = alerteForm
								if 'submitted' in request.GET:
									submitted=True
							return render(request, 'alertes/nouvelle_alerte.html', {
								'form': form,
								'submitted': submitted,
							})