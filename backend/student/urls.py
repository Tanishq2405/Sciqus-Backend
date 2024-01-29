from django.urls import path
from . import views


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('register/', views.register_student, name='register_student'),
    path('student/', views.student_list, name='student_list'),
    path('course/<int:course_id>/', views.students_in_course, name='students_in_course'),
    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    # Add other URL patterns as needed
]
