from django.shortcuts import render
from .models import *
from django.db.models import *

# Create your views here.

def get_students(request):
    computer_students = Students.objects.filter(department__department_name = 'Computer')
    comp_ele_students = Students.objects.filter(department__department_name__in = ['Computer', 'Electrical'])
    studs_exculding_civil = Students.objects.exclude(department__department_name = "Civil")
    stud_ages = Students.objects.values_list('student_name', 'student_age')

    avg_student_age = Students.objects.aggregate(Avg('student_age'))
    print("average age of students:", avg_student_age)

    computer_students_count = computer_students.values('student_age').annotate(Count('student_age'))
    print("computer students age count:", computer_students_count)

    students = Students.objects.all()
    return render(request, 'management/students.html', context={'students': students})
