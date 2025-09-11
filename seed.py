from faker import Faker
import random
from management_app.models import *
from django.db.models import Sum


def generate_departments():
    departments = ['Computer', 'Electrical', 'Civil', 'IT', 'Mechanical']

    for department in departments:
        dep_obj = Department.objects.create(department_name = department)
        dep_obj.save()


def generate_subjects():
    subjects_list = ['C++', 'python', 'java', 'Maths', 'Graphics']

    for subject in subjects_list:
        sub_obj = Subjects.objects.create(subject_name = subject)
        sub_obj.save()



def generate_students(n):
    fake = Faker()
    departments = list(Department.objects.all())

    for _ in range(n):
        department = random.choice(departments)
        student_id = f'STU-0{random.randint(1, 100)}'
        
        fake_name = fake.name()
        fake_email = fake.email()
        fake_age = random.randint(18, 35)
        fake_address = fake.address()

        student_id_obj = StudentID.objects.create(student_id=student_id)

        Students.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name=fake_name,
            student_age=fake_age,
            student_email=fake_email,
            student_address=fake_address
        )


def generate_marks():
    students = Students.objects.all()

    for student in students:
        subjects = Subjects.objects.all()
        for subject in subjects:
            StudentMarks.objects.create(
                student=student,
                subject=subject,
                marks = random.randint(0, 100)
            )


def generate_reportcards():
    ranks = Students.objects.annotate(total_marks=Sum('studentmarks__marks')).order_by('-total_marks')
    i = 1
    for rank in ranks:
        ReportCards.objects.create(
            student=rank,
            student_rank=i
        )
        i += 1