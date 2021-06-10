from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def loginCheck(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    if username=="Goutham" and password=="Nandha":
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")