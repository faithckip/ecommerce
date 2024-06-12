from django.db import models

# Create your models here.
class Product(models.Model):
    pname= models.CharField(max_length=30)
    price = models.IntegerField()
    img = models.ImageField(null =True, blank = True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = 'media.item_images.url'
        except:
            url = ''
        return url
    
