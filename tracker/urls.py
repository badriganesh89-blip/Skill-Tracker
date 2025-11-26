from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Students
    path('add-student/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),

    # Skills
    path('add-skill/', views.add_skill, name='add_skill'),

    # Recommendations
    path('recommend/<int:id>/', views.recommend_jobs, name='recommend_jobs'),

    # Auth
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]
