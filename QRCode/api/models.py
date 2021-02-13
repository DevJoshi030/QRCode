from django.db import models

# Create your models here.


class Restaurant(models.Model):

    name = models.CharField(max_length=200)
    key = models.CharField(max_length=10, unique=True)

    def __str__(self):

        return self.name


class QRCode(models.Model):

    link = models.CharField(max_length=200)
    table_id = models.IntegerField()
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.restaurant} - {self.table_id}'
