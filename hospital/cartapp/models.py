from django.db import models
from django.contrib.auth.models import User

class Hospital(models.Model):
    hospital = models.CharField(max_length=60)
    mobile = models.IntegerField()

    def __str__(self):
        return str(self.hospital)


class Salesperson(models.Model):
    sales = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hospital)
