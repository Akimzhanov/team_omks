from django.db import models
from slugify import slugify


class Brand(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, primary_key=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Smartphone(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=220, primary_key=True, blank=True)
    image = models.ImageField(upload_to='smart_images')
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SmartImage(models.Model):
    image = models.ImageField(upload_to='smart_images/carousel')
    smart = models.ForeignKey(Smartphone, on_delete=models.CASCADE, related_name='smart_images')

