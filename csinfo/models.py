from django.db import models

# Create your models here.


class Torneo(models.Model):
    nombreTorneo = models.CharField(max_length=100)
    locacionTorneo = models.CharField(max_length=100)
    teamsParticipando = models.IntegerField()
    premio = models.IntegerField()
    fechaInicio = models.DateField(verbose_name='fecha_inicio' )
    fechaTermino = models.DateField(verbose_name='fecha_termino')
    topPlayer = models.CharField(max_length=100)
    teamCampeon = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTorneo