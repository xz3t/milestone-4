from django.db import models

# Create your models here.


class About(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=False, blank=False)
    url = models.URLField(
        max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
