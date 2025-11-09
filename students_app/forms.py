from django import forms
from .models import Student, Course

# Course Form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter course name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter course description', 'rows': 3}),
        }


# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'email', 'phone', 'address',
            'gender', 'course', 'profile_pic'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address', 'rows': 3}),
        }
