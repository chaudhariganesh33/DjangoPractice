from faker import Faker
import random
from management_app.models import *


def generate_students(n):
    fake = Faker()
    departments = list(Department.objects.all())

    for _ in range(n):
        department = random.choice(departments)
        student_id = f'STU-0{random.randint(3, 100)}'
        
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


def generate_marks(n):
    students = Students.objects.all()

    for student in students:
        subjects = Subjects.objects.all()
        for subject in subjects:
            StudentMarks.objects.create(
                student=student,
                subject=subject,
                marks = random.randint(0, 100)
            )