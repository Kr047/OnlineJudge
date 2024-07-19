from django.db import models

# Create your models here.
class problem(models.Model):
    statement = models.CharField(max_length = 2000)

    def __str__(self):
        return self.statement
