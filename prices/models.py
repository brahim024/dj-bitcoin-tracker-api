from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=20)
    def __str__(self):
        return str(self.id)
class Prices(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.CharField(max_length=100)
    cap_rank = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 