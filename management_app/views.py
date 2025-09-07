from django.shortcuts import render
from .models import *

# Create your views here.

def get_students(request):

    computer_students = Students.objects.filter(department__department_name = 'Computer')
    print(f"computer_students {computer_students}\n")

    comp_ele_students = Students.objects.filter(department__department_name__in = ['Computer', 'Electrical'])

    studs_exculding_civil = Students.objects.exclude(department__department_name = "Civil")

    stud_ages = Students.objects.values_list('student_name', 'student_age')

    print(f"student_ages {stud_ages}\n")

    students = Students.objects.all()

    return render(request, 'management/students.html', context={'students': students})
