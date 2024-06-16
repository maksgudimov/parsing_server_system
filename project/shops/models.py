from django.db import models


class City(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    street = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.street


class Shop(models.Model):

    name = models.CharField(max_length=100)
    # city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    address = models.ManyToManyField(Address, blank=True)

    def __str__(self):
        return self.name
