from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Students)
admin.site.register(Subjects)

class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(StudentMarks, StudentMarksAdmin)