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


#serializers helps to convert queryset into json strings
from django.core import serializers

#sending email 
from django.core.mail import send_mail
#to send mail to admin
from django.core.mail import mail_admins


#to create random number for OTP
from random import randint

# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request,'gallery.html')

### xhtml2pdf
def final(request, *args, **kwargs):
    if request.method=="POST":
        roll=request.POST.get('roll')
        barsa= request.POST.get('yrs')
        presentation= request.POST.get('presentation')
        quality1 = request.POST.get('quality1')
        quality2 = request.POST.get('quality2')
        eca = request.POST.get('eca')
        project = request.POST.get('project')
        paper = request.POST.get('paper')

        student = StudentData.objects.get(std__roll_number = roll)
        student.years_taught=barsa
        student.presentation= presentation
        student.quality1 = quality1 
        student.quality2 = quality2 
        student.eca = eca
        student.project = project 
        student.paper = paper
        student.is_generated=True
        student.save()
        send_mail('Recommendation Letter', 'congratulation you recieved recommendation letter ,http://127.0.0.1:8000/loginStudent', 'christronaldo9090909@gmail.com', [student.email], fail_silently=False)

    
    template_path = 'print.html'
    context={'student':student }
    
    
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


### xhtml2pdf
def studentfinal(request, *args, **kwargs):
    if request.method=="POST":
        roll=request.POST.get('roll')
        student = StudentData.objects.get(std__roll_number = roll)
   

    template_path = 'print.html'
    context={'student':student }
    
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    ##If Download
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    ## If view
    #response['Content-Disposition'] = 'filename="your_letter.pdf"'

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
                    stdnt = StudentData.objects.get(std__roll_number=roll)
                    return render(request,"student_success.html",{'naam': student.username,"roll":student.roll_number,'letter':stdnt.is_generated})
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
        uemail= request.POST.get('email')

        x= uprof.split("| ")
        id=x[-1]
        prof = TeacherInfo.objects.get(unique_id = id)
        stu = StudentLoginInfo.objects.get(roll_number = uroll)
        
        info = StudentData(name=stu.username , uni=uuni, professor=prof ,std = stu,email=uemail)
        info.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,"student_success.html")


def loginTeacher(request):
    value=0
    if request.method=="POST":
        usern=request.POST.get('username')
        passwo= request.POST.get('password')
        # check if user is real 
        if User.objects.filter(username__exact=usern).exists():
            user = authenticate(username=usern, password=passwo)
            if user is not None:
                login(request,user)
                full_name = request.user.get_full_name()
                x = full_name.split("/")
                unique=x[-1]
                dataharu = StudentData.objects.filter( professor__unique_id=unique)

                #to check if there is request or not on teachers page
                for data in dataharu:
                    if data.is_generated:
                        value+=1
                datakolength=len(dataharu)
                if datakolength==value:
                    check_value=True
                else:
                    check_value=False
                    # to convert database to json objects
                std_dataharu=serializers.serialize("json",StudentData.objects.filter( professor__unique_id=unique))
                
                return render(request, 'Teacher.html',{'student_list':dataharu,'check_value':check_value,'std_dataharu':std_dataharu})
        # A backend authenticated the credentials
            else:
        # No backend authenticated the credentials
                messages.error(request, 'Sorry!  The Password doesnot match.')
                return render(request, 'loginTeacher.html')
        else:
            
            messages.error(request, 'You are not registered as a professor.')
            return render(request, 'loginTeacher.html')
    return render(request, 'loginTeacher.html')
    

    



def logoutUser(request):
    logout(request)
    return redirect("/login")

def forgotPassword(request):
    #generating otp so that it is generated only once 
    OTP_value=OTP_generator(5)
    response= render(request, 'forgotPassword.html')
    response.set_cookie('OTP_value',OTP_value)
    return response



# OTP
def otp(request):
    
    if request.method=="POST"  :
        Usernaam=request.POST.get('username')

        sir= User.objects.get(username = Usernaam)
        full_name = sir.get_full_name()
        print(full_name)
        x=full_name.split("/")
        name=x[0]
        id=x[-1]
        
        if TeacherInfo.objects.filter(unique_id=id).exists():
            master = TeacherInfo.objects.get(unique_id=id)
            
            OTP_value=request.COOKIES.get('OTP_value')
           
            send_mail('OTP ', 'Your OTP for Recoomendation Letter is '+ str(OTP_value),'christronaldo9090909@gmail.com',  [master.email], fail_silently=False)
              
            response= render(request, 'otp.html',{'teacherkonam':master,'OTP_value':OTP_value})
            #making cookies to store and send them to other view page
            
            response.set_cookie('teacher_ko_naam',master)
            response.set_cookie('teacher_ko_username',Usernaam)
            return response


        else:
            messages.error(request, 'Sorry You are not registered as a Professor.')
            return render(request, 'loginTeacher.html')
    
# Otp check
def OTP_check(request):
    if request.method=="POST":
        user_OTP_value=request.POST.get('user_typed_OTP_value')

        #using cookies to obtain otp value and teacher 
        OTP_value=request.COOKIES.get('OTP_value')
        teacher_ko_naam=request.COOKIES.get('teacher_ko_naam')


        if OTP_value==user_OTP_value:
            return render(request, 'validatePassword.html',{'teacher_ko_naam':teacher_ko_naam})
        else:
            messages.error(request, 'Wrong OTP_value')
            return render(request, 'loginTeacher.html')


# #to pass the username and to validate the user

# def validatePassword(request):
#     teacher_ko_naam=request.COOKIES.get('teacher_ko_naam')
#     OTP_value=request.COOKIES.get('OTP_value')
#     return render(request, 'validatePassword.html',{'teacher_ko_naam':teacher_ko_naam, 'OTP_value':OTP_value})


#pwd is changed of corresponding user passed from validatePassword
def changePassword(request):
    
    if request.method=="POST" :
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
      
    if password1==password2:
        #Teacher ko Username using cookies from 'otp' view page
        teacher_ko_user_naam=request.COOKIES.get('teacher_ko_username')

        #changing Pwd
        usr = User.objects.get(username=teacher_ko_user_naam)
        usr.set_password(password1)
        usr.save()
        messages.success(request, 'Password has been changed successfully.')
        return render(request, 'loginTeacher.html')
    else:
        
        return render(request, 'validatePassword.html')




def OTP_generator(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)  
        

#to pass message to admin user
def contact(request):
    
    return render(request, 'contact.html')

def about(request):
    
    return render(request, 'about.html')

def feedback(request):
    
    if request.method=="POST":
        First_name =request.POST.get('first_name')  
        last_name =request.POST.get('last_name')   
        email =request.POST.get('email')  
        feedback =request.POST.get('feedback')   

        message =str(First_name)+"\n"+str(last_name)+"\n"+str(email)+"\n"+str(feedback)

        mail_admins("Feedback", message, fail_silently=False, connection=None, html_message=None)
        send_mail("Reply From Recoomendation Letter Team", "Thank you for your feedback. We will get back to you soon.", " christronaldo9090909@gmail.com",[email],fail_silently=False)
    return render(request, 'contact.html')