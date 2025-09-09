from django.shortcuts import render
from .models import *
from django.db.models import *
from django.core.paginator import Paginator

# Create your views here.

# def get_students(request):
#     computer_students = Students.objects.filter(department__department_name = 'Computer')
#     comp_ele_students = Students.objects.filter(department__department_name__in = ['Computer', 'Electrical'])
#     studs_exculding_civil = Students.objects.exclude(department__department_name = "Civil")
#     stud_ages = Students.objects.values_list('student_name', 'student_age')

#     avg_student_age = Students.objects.aggregate(Avg('student_age'))
#     print("average age of students:", avg_student_age)

#     computer_students_count = computer_students.values('student_age').annotate(Count('student_age'))
#     print("computer students age count:", computer_students_count)

#     students = Students.objects.all()
#     return render(request, 'management/students.html', context={'students': students})


def get_students(request):
    students = Students.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        students = students.filter(Q(student_name__icontains=search) | Q(student_email__icontains=search))
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'management/students.html', context={'students': page_object})


def see_marks(request, student_id):
    studentmarks = StudentMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = studentmarks.aggregate(total_marks = Sum('marks'))
    return render(request, 'management/marks.html', context={'marks': studentmarks, 'total_marks': total_marks})