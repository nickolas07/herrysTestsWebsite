from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=300, default='')
    fach = models.CharField(max_length=100, default='Mathematik')
    jahrgang = models.IntegerField()
    aufgaben = models.JSONField(default=dict)

    def __str__(self):
        return self.name
