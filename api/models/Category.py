from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)


    def get_absolute_urel(self):
        return  f'/{self.slug}/'
    
    
    def __str__(self):
        return self.name

    