from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    tags=models.CharField(max_length=10,blank=True)
    featured=models.BooleanField(default=False)
    image=models.URLField(max_length=200)

    def __str__(self):
        return self.name
    