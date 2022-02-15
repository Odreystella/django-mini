from django.db import models


class Bread(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bread"


class Topping(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "toppings"


class Cheese(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cheeses"


class Sauce(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sauces"


class Sandwich(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    sauces = models.ManyToManyField(Sauce)
    price = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "sandwiches"
