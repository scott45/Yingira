from django.db import models


class User(models.Model):
    Names = models.CharField(max_length=100, blank=False)
    Email = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '{} | {} '.format(self.Names, self.Email)


class Store(models.Model):
    Title = models.CharField(max_length=30)
    Owner = models.ForeignKey(User)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.Title)


class Product(models.Model):
    Name = models.CharField(max_length=30)
    Category = models.ForeignKey(Store, default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.Name)
