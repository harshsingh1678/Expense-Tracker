from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Earning(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Expense(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)