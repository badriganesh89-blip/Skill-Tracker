from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.name} - {self.skill_name}"


class Job(models.Model):
    job_title = models.CharField(max_length=200)
    required_skills = models.TextField()

    def __str__(self):
        return self.job_title