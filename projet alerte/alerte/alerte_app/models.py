from django.db import models

class localisation(models.Model):
    adresse = models.CharField('Adresse', max_length=150)
    description = models.TextField('Description', blank=True)
    def __str__(self):
        return self.adresse

class police_centrale(models.Model):
    tel = models.IntegerField("Telephone de la police")
    adresse = models.CharField("Adresse de la police", max_length=150)
    def __str__(self):
        return self.adresse

class user(models.Model):
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
    adresse = models.CharField(' Adresse', max_length=120)
    tel = models.IntegerField("Telephone")
    def __str__(self):
        return self.nom

class alerte(models.Model):
    heure = models.DateTimeField("Date infraction", auto_now_add=True)
    description = models.TextField('Description alerte', blank=True)
    user=models.ForeignKey(user, blank=False, on_delete=models.CASCADE)		
    localisation=models.ForeignKey(localisation, blank=False, on_delete=models.CASCADE)
    police_centrale=models.ForeignKey(police_centrale, blank=False, on_delete=models.CASCADE)							
    def __str__(self):
        return self.description

