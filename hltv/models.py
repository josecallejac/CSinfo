from django.db import models

# Create your models here.



#class Producto(models.Model):
#    nombre = models.CharField(max_length=100)
#    descripcion = models.TextField()
#    precio = models.DecimalField(max_digits=8, decimal_places=2)
#    fecha_creacion = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return self.nombre



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
    logo = models.ImageField(verbose_name='logo')

    def __str__(self):
        return self.nameTeam



class Noticias(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    link = models.URLField(verbose_name='link')
    time = models.DateTimeField(verbose_name='time')

    def __str__(self):
        return self.title
    

""" class Market(models.Model):
    nameWeapon = models.CharField(max_length=100)
    defWeapon = models.Choices()
    qualityWeapon = models.Choices()
    price = models.IntegerField(max_length=100)
    containerWeapon = models.CharField(max_length=100)
    collectionsWeapon = models.CharField(max_length=100)

     def __str__(self):
        return self.nameWeapon

 """


"""  class Torneos(models.Model):
    nombreTorneo = models.CharField(max_length=100)
    locacionTorneo = models.CharField(max_length=100)
    teamsParticipando = models.IntegerField(max_length=10)
    premio = models.IntegerField(max_length=10)
    fechaInicio = models.DateField(verbose_name='fecha_inicio' )
    fechaTermino = models.DateField(verbose_name='fecha_termino')
    topPlayers = models.CharField(max_length=100)
    topTeams = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTorneo """
    
