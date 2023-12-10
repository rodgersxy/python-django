# listings/models.py

from django.db import models




class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class AdditionalImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  # Many-to-one relationship
    image = models.ImageField(upload_to='additional_images/%Y/%m/%d/')


    def __str__(self):
        return f"{self.listing.title} - Additional Image"
