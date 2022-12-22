from django.db import models

class Travel(models.Model):
    title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, default='+996')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    transport = models.CharField(max_length=50)
    living = models.TextField(max_length=100) #Условие проживания
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.title}'

class TravelImages(models.Model):
    picture = models.ImageField(upload_to='travel_images/carousel')
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, related_name='travel_images')

