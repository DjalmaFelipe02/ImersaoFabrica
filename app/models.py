from django.db import models


ENSINO_MEDIO = 'Ensino Médio'
ENSINO_FUNDAMENTAL = 'Ensino Fundamental'
INFANTIL = 'Infantil'
FACULDADE = 'Faculdade'

PERIOD_CHOICES = [
    (ENSINO_MEDIO, ENSINO_MEDIO),
    (ENSINO_FUNDAMENTAL, ENSINO_FUNDAMENTAL),
    (INFANTIL, INFANTIL),
    (FACULDADE, FACULDADE)
]

class Student(models.Model):
    name = models.CharField(max_length=45)
    note = models.DecimalField(decimal_places=2,max_digits=4)
    age = models.IntegerField()
    period = models.CharField(max_length=30,choices=PERIOD_CHOICES)
    data = models.DateField(auto_now_add=True)
    data_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

