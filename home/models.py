from django.db import models
from django.db.models.deletion import CASCADE

class StudentLoginInfo(models.Model):
    username = models.CharField(max_length=120,null=True,blank=True)
    roll_number = models.CharField(max_length=9,null=True,blank=True)
    department = models.CharField(max_length=100 ,null=True,blank=True)
    program = models.CharField(max_length=50 , default="null",null=True,blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10 , default="null",null=True,blank=True)
    def __str__(self):
        return str(self.username)


class Subject(models.Model):
    name= models.CharField(max_length=150, blank=True,null=True)
    def __str__(self):
        return str(self.name)


class TeacherInfo(models.Model):
    unique_id = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=40,null=True,blank=True)
    title = models.CharField(max_length=30,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField()
    department = models.CharField(max_length=100 , default="null",null=True,blank=True)
    images = models.ImageField(upload_to='images/', blank=True, default="cute_baby.gif")
    subjects = models.ManyToManyField(Subject )

    def __str__(self):
        return str(self.name)

class StudentData(models.Model): 
    name = models.CharField(max_length=122,null=True,blank=True)
    uni = models.CharField(max_length=122,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    professor = models.ForeignKey(TeacherInfo, on_delete= CASCADE)
    std = models.ForeignKey(StudentLoginInfo, on_delete= CASCADE)
    is_generated = models.BooleanField(default=False) 
    years_taught= models.CharField(max_length=2, null=True, blank=True)
    
    gpa = models.CharField(max_length=5 ,default="null")
    is_pro = models.CharField(max_length=3,default="null")
    final_project = models.CharField(max_length=100)
    project1 = models.CharField(max_length=100,default="null")
    project2 = models.CharField(max_length=100,default="null")
    paper = models.CharField(max_length=3,default="null")
    paper_link = models.CharField(max_length=200,default="null")
    subjects= models.CharField(max_length=500, null=True, blank=True)
    


    # teacher side
    presentation= models.CharField(max_length=15,null=True,blank=True)
    extracirricular= models.CharField(max_length=15,null=True,blank=True)
    academics= models.CharField(max_length=15,null=True,blank=True)
    quality= models.CharField(max_length=15,null=True,blank=True)

        #personal qualities
    leadership = models.BooleanField(default=False) 
    hardworking = models.BooleanField(default=False) 
    social = models.BooleanField(default=False) 
    teamwork = models.BooleanField(default=False) 
    friendly = models.BooleanField(default=False) 
    

        #other qualities

    deployed = models.BooleanField(default=False)
    published = models.BooleanField(default=False) 
    intern = models.BooleanField(default=False) 
    


    def __str__(self):
        return str(self.name)

