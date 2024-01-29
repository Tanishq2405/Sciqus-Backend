# forms.py in yourapp

from django import forms
from .models import Student, Course

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course',]  # Add other fields as needed

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course']  # Add other fields from Student model as needed

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

