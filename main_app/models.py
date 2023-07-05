from django.db import models

# Create your models here.
class Brand(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_brand = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class Collection(models.Model):

    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="collections")

    def __str__(self):
        return self.title

class Favorites(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    Collections = models.ManyToManyField(Collection)

    def __str__(self):
        return self.title
