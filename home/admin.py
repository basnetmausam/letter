from django.contrib import admin
from home.models import StudentData, StudentLoginInfo

# Register your models here.
admin.site.register(StudentLoginInfo)
admin.site.register(StudentData)

