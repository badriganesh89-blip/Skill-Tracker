from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Student, Skill


# HOME PAGE
def home(request):
    return render(request, 'tracker/home.html')


# ADD STUDENT
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            course=course
        )

        return redirect('home')

    return render(request, 'tracker/add_student.html')


# ADD SKILL
def add_skill(request):
    students = Student.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        skill_name = request.POST.get('skill')

        student = get_object_or_404(Student, id=student_id)

        Skill.objects.create(
            student=student,
            skill_name=skill_name
        )

        return redirect('home')

    return render(request, 'tracker/add_skill.html', {'students': students})


# STUDENT LIST
def student_list(request):
    students = Student.objects.all()
    return render(request, 'tracker/student_list.html', {'students': students})


# STUDENT DETAIL
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    skills = Skill.objects.filter(student=student)
    return render(request, 'tracker/student_detail.html', {'student': student, 'skills': skills})


# JOB RECOMMENDATION
def recommend_jobs(request, id):
    student = get_object_or_404(Student, id=id)

    student_skills = Skill.objects.filter(student=student).values_list('skill_name', flat=True)

    recommendations = []

    if 'Python' in student_skills:
        recommendations.append('Python Developer at TechCorp')

    if 'Django' in student_skills:
        recommendations.append('Django Developer at WebSolutions')

    if 'JavaScript' in student_skills:
        recommendations.append('Frontend Developer at CreativeApps')

    return render(request, 'tracker/recommend.html', {
        'student': student,
        'recommendations': recommendations
    })


# EDIT STUDENT
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()

        return redirect('student_detail', student.id)

    return render(request, 'tracker/edit_student.html', {'student': student})


# DELETE STUDENT
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'tracker/delete_student.html', {'student': student})


# LOGIN USER
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'tracker/login.html', {'error': 'Invalid username or password'})

    return render(request, 'tracker/login.html')


# SIGNUP USER
def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('login')

    return render(request, 'tracker/signup.html')


# LOGOUT USER
def logout_user(request):
    logout(request) 
    return redirect('login')


# DASHBOARD (PROTECTED)
@login_required(login_url='login')
def dashboard(request):
    total_students = Student.objects.count()
    total_skills = Skill.objects.count()

    return render(request, 'tracker/dashboard.html', {
        'total_students': total_students,
        'total_skills': total_skills,
    })
