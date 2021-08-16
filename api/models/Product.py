from os import name
from django.db import models
from .Category import *
from django.core.files import File
from io import BytesIO
from PIL import Image


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', blank=True, null=True, on_delete= models.SET_NULL)
    name =  models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug  = models.SlugField()

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://localhost:8000' + self.image.url
        else:
            return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://localhost:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://localhost:8000' + self.thumbnail.url
            else:
                return ''

    def make_thubnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumnail = File(thumb_io, name=image.name)

        return thumnail
 
            