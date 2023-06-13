from django.db import models
from model_utils import Choices
from django.conf import settings
import os 






class Player(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    mapsPlayed = models.IntegerField(verbose_name='mapsplayed')
    kd = models.DecimalField(verbose_name='kd', max_digits=5, decimal_places=2)
    rating = models.DecimalField(verbose_name='rating', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nickname

    
class Teams(models.Model):
    id_team = models.AutoField(primary_key=True)
    nameTeam = models.CharField(max_length=50)
    ranking = models.IntegerField(verbose_name='ranking')
    logo = models.ImageField(upload_to='media')
    players = models.CharField(max_length=250)

    def __str__(self):
        return self.nameTeam



class Noticias(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    link = models.URLField(verbose_name='link')
    time = models.DateTimeField(verbose_name='time')

    def __str__(self):
        return self.title
    


    
class Market(models.Model):
    WTYPE_1 = 'Pistols'
    WTYPE_2 = 'Rifles'
    WTYPE_3 = 'SMG'
    WTYPE_4 = 'Shotguns'
    WTYPE_5 = 'Knifes'
    WTYPE_6 = 'Gloves'

    CHOICES = (
        (WTYPE_1, 'Pistols'),
        (WTYPE_2, 'Rifles'),
        (WTYPE_3, 'SMG'),
        (WTYPE_4, 'Shotguns'),
        (WTYPE_5, 'Knifes'),
        (WTYPE_6, 'Gloves'),
    )
    choice_field = models.CharField(max_length=50, choices=CHOICES)
    def __str__(self):
        return self.choice_field 


class Armas(models.Model):
    market = models.OneToOneField(Market, on_delete=models.CASCADE)
    nameSkin = models.CharField(max_length=100)
    DWEAPON1 = 'Classified'
    DWEAPON2 = 'Restricted'
    DWEAPON3 = 'Mil-spec'
    DWEAPON4 = 'Covert'
    DWEAPON5 = 'Industrial'
    DWEAPON6 = 'Consumer'

    OPCIONESARMAS = (
        (DWEAPON1, 'Classified'),
        (DWEAPON2, 'Restricted'),
        (DWEAPON3, 'Mil-spec'),
        (DWEAPON4, 'Covert'),
        (DWEAPON5, 'Industrial'),
        (DWEAPON6, 'Consumer'),
    )
    defWeapon = models.CharField(max_length=50, choices=OPCIONESARMAS)

    QWEAPON1 = 'FN'
    QWEAPON2 = 'MW'
    QWEAPON3 = 'FT'
    QWEAPON4 = 'WW'
    QWEAPON5 = 'BS'
    QWEAPON6 = 'ST FN'
    QWEAPON7 = 'ST MW'
    QWEAPON8 = 'ST FT'
    QWEAPON9 = 'ST WW'
    QWEAPON10 = 'ST BS'

    OPCIONESQUALITY = (
        (QWEAPON1, 'FN'),
        (QWEAPON2, 'MW'),
        (QWEAPON3, 'FT'),
        (QWEAPON4, 'WW'),
        (QWEAPON5, 'BS'),
        (QWEAPON6, 'ST FN'),
        (QWEAPON7, 'ST MW'),
        (QWEAPON8, 'ST FT'),
        (QWEAPON9, 'ST WW'),
        (QWEAPON10, 'ST BS'),
    )
    qualityWeapon = models.CharField(max_length=50, choices=OPCIONESQUALITY)
    containerWeapon = models.CharField(max_length=100)
    collectionsWeapon = models.CharField(max_length=100)
    imagenArma = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.nameSkin 





""" class Torneos(models.Model):
    nombreTorneo = models.CharField(max_length=100)
    locacionTorneo = models.CharField(max_length=100)
    teamsParticipando = models.IntegerField()
    premio = models.IntegerField()
    fechaInicio = models.DateField(verbose_name='fecha_inicio' )
    fechaTermino = models.DateField(verbose_name='fecha_termino')
    topPlayer = models.CharField(max_length=100)
    teamCampeon = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTorneo  """
    
