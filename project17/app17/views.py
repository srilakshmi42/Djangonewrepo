from django.shortcuts import render
#from django.http import HttpResponse
from app17.models import Registration

def showMainPage(request):
    return render(request,"main.html")

def showRegisterPage(request):
    if request.method == "POST":
        n = request.POST.get("name")
        con = request.POST.get("contact")
        loc = request.POST.get("location")
        email = request.POST.get("email")
        password = request.POST.get("password")
        Registration(name=n,contact=con,location=loc,email=email,password=password).save()
        return render(request,"register.html",{"message":"Registration is Done"})

    else:
        return render(request,"register.html")


def showLoginPage(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            stu_obj=Registration.objects.get(email=email,password=password)
            return render(request,"welcome.html")
        except Registration.DoesNotExist:
            return render(request,"login.html",{"error_message":"invalid user"})
    else:
        return render(request,'login.html')