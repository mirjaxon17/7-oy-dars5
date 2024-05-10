from django.db import models


class Adress(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Admins(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.adress}{self.phone_number}"