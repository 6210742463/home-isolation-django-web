from django.db import models
from django.contrib.auth.models import User

class Petients(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.CharField(max_length=4, null=True, blank=True)
    disease = models.TextField(null=True, blank=True)
    defeat = models.TextField(null=True, blank=True)

class Status(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    status = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.status}"

class PulseDairy(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    spo2 = models.IntegerField(null = True, blank = True)
    temp = models.DecimalField(max_digits=50, decimal_places=2, null = True, blank = True)
    beat = models.IntegerField(null = True, blank = True)

    # green symptom
    gs1 = models.CharField(max_length=50, null=True, blank=True)
    gs2 = models.CharField(max_length=50, null=True, blank=True)
    gs3 = models.CharField(max_length=50, null=True, blank=True)
    gs4 = models.CharField(max_length=50, null=True, blank=True)
    gs5 = models.CharField(max_length=50, null=True, blank=True)

    # yellow symptom
    ys1 = models.CharField(max_length=50, null=True, blank=True)
    ys2 = models.CharField(max_length=50, null=True, blank=True)
    ys3 = models.CharField(max_length=50, null=True, blank=True)
    ys4 = models.CharField(max_length=50, null=True, blank=True)

    # red symptom
    rs1 = models.CharField(max_length=50, null=True, blank=True)
    rs2 = models.CharField(max_length=50, null=True, blank=True)
    rs3 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.created}"



