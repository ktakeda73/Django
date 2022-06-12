from django.db import models

class Dispatch(models.Model):
    name=models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

class Office(models.Model):
    name=models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(
        max_length=30)
    dispatch = models.ForeignKey(Dispatch,on_delete=models.SET_NULL,null=True)
    office = models.ManyToManyField(Office,related_name='employee')

    def __str__(self):
        return self.name