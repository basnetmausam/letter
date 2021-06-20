from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login
from django.contrib.auth.forms import AuthenticationForm
from .models import StudentLoginInfo
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginStudent(request):
    if request.method=="POST":
        usern=request.POST.get('name')
        roll= request.POST.get('roll')
        dob= request.POST.get('dob')
    # check if user is real
    
     #   student = StudentLoginInfo.objects.get(username__exact=usern)
        if StudentLoginInfo.objects.filter(username__exact=usern).exists():
            student = StudentLoginInfo.objects.get(username__exact=usern)
            if (student.roll_number==roll and str(student.dob)==dob):
                return render(request,'Student.html')
            else:
                messages.error(request, 'Sorry!  The Credentials doesnot match.')
                return render(request, 'loginStudent.html')
        else:
            messages.error(request,'Seems Like You are not the student of Pulchowk')
            return render(request, 'loginStudent.html')
    return render(request, 'loginStudent.html')


def loginTeacher(request):
    if request.method=="POST":
        usern=request.POST.get('username')
        passwo= request.POST.get('password')
    # check if user is real
        user = authenticate(username=usern, password=passwo)
        if user is not None:
            login(request,user)
            return render(request, 'Teacher.html')
    # A backend authenticated the credentials
        else:
    # No backend authenticated the credentials
            messages.error(request, 'Sorry You are not registered as a Professor.')
            return render(request, 'loginTeacher.html')
    return render(request, 'loginTeacher.html')



def logoutUser(request):
    logout(request)
    return redirect("/login")