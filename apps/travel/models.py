from django.db import models

class Travel(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150)
    price = models.DecimalField(max_digits=18,decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title