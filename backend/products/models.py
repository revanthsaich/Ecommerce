from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
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
    slug = models.SlugField(max_length=255, blank=True)
    def save(self, *args, **kwargs):
        # Automatically generate a slug from the product name if not already set
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Products.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    