from django.db import models


class Bread(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cheese(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Sauce(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    sauces = models.ManyToManyField(Sauce)
    price = models.PositiveSmallIntegerField()
