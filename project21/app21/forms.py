from django import forms
from app21.models import StudentModel,CourseModel

class CourseForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = CourseModel

class StudentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = StudentModel