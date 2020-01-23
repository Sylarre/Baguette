from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Reteta(models.Model):
    titlu = models.CharField(max_length=140)
    continut = models.TextField()
    data_adaugare = models.DateTimeField(default=timezone.now)
    #timp_executie = models.PositiveIntegerField(default=0)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titlu

    def get_absolute_url(self):
        return reverse('reteta-detail', kwargs={'pk':self.pk})