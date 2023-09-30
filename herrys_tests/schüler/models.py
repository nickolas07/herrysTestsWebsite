from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=300)
    jahrgang = models.IntegerField()

    def __str__(self):
        return self.name
