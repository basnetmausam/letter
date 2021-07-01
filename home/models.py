from django.db import models
from django.db.models.deletion import CASCADE

class StudentLoginInfo(models.Model):
    username = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=9)
    dob = models.DateField()


    def __str__(self):
        return str(self.username)

class TeacherInfo(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)

class StudentData(models.Model):
    name = models.CharField(max_length=122)
    gpa = models.CharField(max_length=12)
    uni = models.CharField(max_length=122)
    professor = models.ForeignKey(TeacherInfo, on_delete= CASCADE)



    def __str__(self):
        return str(self.name)