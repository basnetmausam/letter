from django.contrib import admin
from django.urls import path ,include
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('loginStudent', views.loginStudent, name='loginStudent'),
    path('loginTeacher', views.loginTeacher, name='loginTeacher'),
    path('logout', views.logoutUser, name='logout'),
    path('studentSuccess', views.studentSuccess, name='StudentSuccess'),
    path('makeLetter', views.make_letter, name='MakeLetter'),
    path('final', views.final, name='Final'),
    path('gallery', views.gallery, name='Gallery'),
    path('studentfinal', views.studentfinal, name='StudentFinal'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    # path('validatePassword', views.validatePassword, name='validatePassword'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('otp', views.otp, name='otp'),
    path('OTP_check', views.OTP_check, name='OTP_check'),






]

