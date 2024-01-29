from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistrationForm
from .forms import StudentUpdateForm
from .models import Student
from django.db import transaction


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or any other page
    else:
        form = StudentRegistrationForm()

    return render(request, 'student/registration_template.html', {'form': form})

# views.py in yourapp
from .models import Student

def student_list(request):
    students = Student.objects.select_related('course').all()
    # Use select_related to fetch related course information in a single query

    context = {'students': students}
    return render(request, 'student/student_list.html', context)

# views.py in yourapp
from .models import Student, Course

def students_in_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = Student.objects.filter(course=course)

    context = {'course': course, 'students': students}
    return render(request, 'student/students_in_course.html', context)

@transaction.atomic
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'student/edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        # Delete the student
        student.delete()

        # Redirect to the list of students or any other page
        return redirect('student_list')

    return render(request, 'student/delete_student.html', {'student': student})