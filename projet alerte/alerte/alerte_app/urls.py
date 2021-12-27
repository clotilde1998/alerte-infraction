from django.urls import path
						
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('listeuser', views.listeuser, name='listeuser'),
	path('localisationlist', views.localisationlist, name='localisationlist'),
	path('policelist', views.policelist, name='policelist'),
	path('alertelist', views.alertelist, name='alertelist'),
	path('nouvelle_alerte', views.nouvelle_alerte, name='nouvelle_alerte'),
		
]