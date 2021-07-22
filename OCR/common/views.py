from django.shortcuts import render
from student.models import RegistrationModel
from django.shortcuts import redirect
from common.utils import sendTextMessage
from random import randint
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages

def showCommonPage(request):
    return render(request,"common/index.html")

def showStudentPage(request):
    return render(request,'common/student.html')

def studentRegistration(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        contact = request.POST.get("student_contact")
        email = request.POST.get("student_email")
        password = request.POST.get("student_password")

        record = RegistrationModel.objects.filter(Q(contact=contact) | Q(email=email))
        print(record)
        if record:
            return render(request, 'common/student.html', {"data": [name, contact, email, "Already exist this contact or email"]})
        else:
            otp = randint(100000,999999)
            message='''Thanks for Registration with Sathya,
            To finish the Registration Use the Given OTP
            Your OTP:'''+str(otp)
            if sendTextMessage(message,contact):
                RegistrationModel(name=name,contact=contact,email=email,password=password,otp=otp).save()
                messages.success(request,contact)
                return redirect('student_otp')
            else:
                return render(request,'common/student.html', {"data": [name, contact, email, "Wrong contact no"]})

    else:
        showStudentPage(request)

def openStudentOtp(request):

    return render(request,"common/otp.html")

def studentLoginCheck(request):
    if request.method=="POST":
        email = request.POST.get("student_emai")
        password = request.POST.get('student_password')
        return HttpResponse("under Development ")
    else:
        return render(request, "common/student.html")

def validateOtp(request):
    contact = request.POST.get("contact")
    sotp = request.POST.get("student_otp")

    try:
        record = RegistrationModel.objects.get(contact=contact,otp=sotp)
        record.status = 'Active'
        record.save()
        return render(request, "common/student.html", {"message":"Thanks for Registration, Please Login"})
    except RegistrationModel.DoesNotExist:
        messages.success(request,contact)
        return redirect('student_otp')



def showFacultyPage(request):
    return render(request, 'common/faculty.html')






















