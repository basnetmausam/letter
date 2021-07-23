from django.db import models
from django.db.models.deletion import CASCADE

class StudentLoginInfo(models.Model):
    username = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=9)
    department = models.CharField(max_length=100 , default="null")
    program = models.CharField(max_length=50 , default="null")


    dob = models.DateField()

    def __str__(self):
        return str(self.username)

class TeacherInfo(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=100 , default="null")


    def __str__(self):
        return str(self.name)

class StudentData(models.Model):
    name = models.CharField(max_length=122)
    uni = models.CharField(max_length=122)
    email = models.EmailField(null=True)
    professor = models.ForeignKey(TeacherInfo, on_delete= CASCADE)
    std = models.ForeignKey(StudentLoginInfo, on_delete= CASCADE)
    is_generated = models.BooleanField(default=False) 
    years_taught= models.CharField(max_length=2)
    presentation= models.CharField(max_length=15)
    quality1 = models.CharField(max_length=20)
    quality2 = models.CharField(max_length=20)
    eca = models.CharField(max_length=3)
    project = models.CharField(max_length=100)
    paper = models.CharField(max_length=3)
    


    def __str__(self):
        return str(self.name)

