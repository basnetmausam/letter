import datetime
from django.db.models.fields import DateTimeField
from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login
from django.contrib.auth.forms import AuthenticationForm
from .models import StudentLoginInfo, StudentData,TeacherInfo
from django.contrib import messages
# imports from xhtml
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request,'gallery.html')

### xhtml2pdf
def final(request, *args, **kwargs):
    if request.method=="POST":
        name=request.POST.get('name')
        barsa= request.POST.get('yrs')
        presentation= request.POST.get('presentation')
        quality1 = request.POST.get('quality1')
        quality2 = request.POST.get('quality2')
        eca = request.POST.get('eca')
        project = request.POST.get('project')
        paper = request.POST.get('paper')


        student = StudentData.objects.get(name=name)

        student.is_generated=True
        student.save()


    
    

    template_path = 'print.html'
    context={'years':barsa , 'presentation':presentation , 'student':student , 'quality1':quality1, 
                'quality2':quality2, 'eca':eca, project:'project' , 'paper':paper}
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    ## If Download
#    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    ## If view
    response['Content-Disposition'] = 'filename="your_letter.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def loginStudent(request):
    if request.method=="POST":
        usern=request.POST.get('name')
        roll= request.POST.get('roll')
        dob= request.POST.get('dob')

        if StudentLoginInfo.objects.filter(username__exact=usern).exists():
            student = StudentLoginInfo.objects.get(roll_number__exact=roll)
            if (student.username==usern and str(student.dob)==dob):
                teachers = TeacherInfo.objects.filter(department = student.department)
                if StudentData.objects.filter(std__roll_number=roll).exists():
                    return render(request,"student_success.html",{'naam': student.username,"roll":student.roll_number})
                else:
                    return render(request,'Student.html',{'naam': student.username , 'teachers':teachers,"roll":student.roll_number})
                         
            else:
                messages.error(request, 'Sorry!  The Credentials doesnot match.')
                return render(request, 'loginStudent.html')
        else:
            messages.error(request,'Seems Like You are not the student of Pulchowk')
            return render(request, 'loginStudent.html')
    return render(request, 'loginStudent.html')

def make_letter(request):
    if request.method=="POST":
        roll=request.POST.get('roll')
    
    stu = StudentLoginInfo.objects.get(roll_number=roll)
    
    return render(request, 'formTeacher.html',{'naam':stu.username , 'roll':roll})



def studentSuccess(request):
    if request.method=="POST":
        uuni= request.POST.get('university')
        uprof= request.POST.get('prof')
        uroll= request.POST.get('roll') 

        prof = TeacherInfo.objects.get(name__exact = uprof)
        stu = StudentLoginInfo.objects.get(roll_number = uroll)
        
        info = StudentData(name=stu.username , uni=uuni, professor=prof ,std = stu)
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
            dataharu = StudentData.objects.filter(is_generated=False , professor__name=sir_name)
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