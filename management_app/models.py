from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name
    
    class Meta:
        ordering = ['department_name']

class StudentID(models.Model):
    student_id = models.CharField(max_length=20)

    def __str__(self):
        return self.student_id
    
class Students(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = 'Student Information'


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name
    
    class Meta:
        ordering = ['subject_name']


class StudentMarks(models.Model):
    student = models.ForeignKey(Students, related_name='student', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.student_name} - {self.subject.subject_name} : {self.marks}"
    
    class Meta:
        unique_together = ['student', 'subject']