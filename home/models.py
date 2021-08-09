from django.db import models
from django.db.models.deletion import CASCADE

class StudentLoginInfo(models.Model):
    username = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=9)
    department = models.CharField(max_length=100 , default="null")
    program = models.CharField(max_length=50 , default="null")
    dob = models.DateField()
    gender = models.CharField(max_length=10 , default="null")
    def __str__(self):
        return str(self.username)

class TeacherInfo(models.Model):
    unique_id = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=100 , default="null")
    images = models.ImageField(upload_to='images/', blank=True, default="cute_baby.gif")
    subject1 = models.CharField(max_length=100, default="null")
    subject2 = models.CharField(max_length=100, default="null")
    subject3 = models.CharField(max_length=100, default="null")
    subject4 = models.CharField(max_length=100, default="null")
    subject5 = models.CharField(max_length=100, default="null")

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
    
    gpa = models.CharField(max_length=5 ,default="null")
    is_pro = models.CharField(max_length=3,default="null")
    final_project = models.CharField(max_length=100)
    project1 = models.CharField(max_length=100,default="null")
    project2 = models.CharField(max_length=100,default="null")
    paper = models.CharField(max_length=3,default="null")
    paper_link = models.CharField(max_length=200,default="null")

    # teacher side
    presentation= models.CharField(max_length=15)
    quality1 = models.CharField(max_length=20)
    quality2 = models.CharField(max_length=20)
    quality3 = models.CharField(max_length=20)
    quality4 = models.CharField(max_length=20)
    eca = models.CharField(max_length=3)

    


    def __str__(self):
        return str(self.name)

