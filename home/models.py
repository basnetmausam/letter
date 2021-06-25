from django.db import models

class StudentLoginInfo(models.Model):
    username = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=9)
    dob = models.DateField()


    def __str__(self):
        return str(self.username)

class StudentData(models.Model):
    name = models.CharField(max_length=122)
    gpa = models.CharField(max_length=12)
    uni = models.CharField(max_length=122)
    professor = models.CharField(max_length=122)


    def __str__(self):
        return str(self.name)