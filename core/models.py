from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 500)
    price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to = "productos", null=True)

    def __str__(self):
        return self.name