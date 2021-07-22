from django.shortcuts import render,redirect
from app21.forms import StudentForm
from app21.forms import CourseForm
from app21.models import StudentModel
from app21.models import CourseModel

def showIndex(request):
    course = CourseForm(request.POST)
    if request.method == "POST":
        course.save()
        return redirect('main')
    else:
        return render(request, "index.html", {"c_form":course, "all_courses":CourseModel.objects.all()})

def showStudent(request):
    result = CourseModel.objects.all()
    if result:
        return render(request, 'student.html', {"s_form": StudentForm()})
    else:
        return render(request,'student.html',{"error":"Please Add Course"})
