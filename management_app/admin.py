from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Students)
admin.site.register(Subjects)

class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(StudentMarks, StudentMarksAdmin)

class ReportCardsAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card']

    def total_marks(self, obj):
        subject_marks = StudentMarks.objects.filter(student = obj.student)
        marks = (subject_marks.aggregate(marks = Sum('marks')))
        return marks['marks']

admin.site.register(ReportCards, ReportCardsAdmin)