from django.db import models

class StudentLoginInfo(models.Model):
    username = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=9)
    dob = models.DateField()


    def __str__(self):
        return str(self.username)

