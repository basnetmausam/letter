import datetime
from django.db.models.fields import DateTimeField
from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login
from django.contrib.auth.forms import AuthenticationForm
from .models import StudentLoginInfo, StudentData,TeacherInfo
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginStudent(request):
    if request.method=="POST":
        usern=request.POST.get('name')
        roll= request.POST.get('roll')
        dob= request.POST.get('dob')

        if StudentLoginInfo.objects.filter(username__exact=usern).exists():
            student = StudentLoginInfo.objects.get(username__exact=usern)
            if (student.roll_number==roll and str(student.dob)==dob):
                if StudentData.objects.filter(name__exact=usern).exists():
                    return render(request,"student_success.html",{'naam': student.username})
                else:
                    return render(request,'Student.html',{'naam': student.username})
                         
            else:
                messages.error(request, 'Sorry!  The Credentials doesnot match.')
                return render(request, 'loginStudent.html')
        else:
            messages.error(request,'Seems Like You are not the student of Pulchowk')
            return render(request, 'loginStudent.html')
    return render(request, 'loginStudent.html')

def make_letter(request):
    if request.method=="POST":
        name=request.POST.get('naam')
    
    return render(request, 'formTeacher.html',{'naam':name})




def studentSuccess(request):
    if request.method=="POST":
        uname=request.POST.get('name')
        ugpa= request.POST.get('gpa')
        uuni= request.POST.get('university')
        uprof= request.POST.get('prof')

        prof = TeacherInfo.objects.get(name__exact = uprof)
        
        info = StudentData(name=uname , gpa=ugpa, uni=uuni, professor=prof)
        info.save()
     #   messages.success(request, 'Your message has been sent.')
    return render(request,"student_success.html")


def loginTeacher(request):
    if request.method=="POST":
        usern=request.POST.get('username')
        passwo= request.POST.get('password')
    # check if user is real
        user = authenticate(username=usern, password=passwo)
        if user is not None:
            login(request,user)
            sir_name=usern.replace("_", " ")
            dataharu=StudentData.objects.filter(professor__name=sir_name)
            return render(request, 'Teacher.html',{'student_list':dataharu})
    # A backend authenticated the credentials
        else:
    # No backend authenticated the credentials
            messages.error(request, 'Sorry You are not registered as a Professor.')
            return render(request, 'loginTeacher.html')
    return render(request, 'loginTeacher.html')



def logoutUser(request):
    logout(request)
    return redirect("/login")