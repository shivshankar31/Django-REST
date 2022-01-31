from django.db import models

# Create your models here.

class empModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id + self.name + self.location + self.salary