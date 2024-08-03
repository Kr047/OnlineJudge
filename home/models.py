from django.db import models

# Create your models here.
class problem(models.Model):
    statement = models.CharField(max_length = 2000)
    question = models.CharField(max_length=10000,default="Lorem Ipsum")

    def __str__(self):
        return self.statement