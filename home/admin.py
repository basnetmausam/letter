from django.contrib import admin
from home.models import StudentData, StudentLoginInfo, TeacherInfo

# Register your models here.
admin.site.register(StudentLoginInfo)
admin.site.register(StudentData)
admin.site.register(TeacherInfo)

