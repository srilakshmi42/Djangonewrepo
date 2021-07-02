from django.shortcuts import render

def showIndex(request):
    if request.method=="POST":
        username=request.POST.get("t1")
        password=request.POST.get("t2")
        type=request.POST.get("ty")
        if username=="Ravi" and password=="ravi1234@" and type=="admin":
            return render(request,"index.html",{"message":"admin"})
        elif username=="Ravi" and password=="kumar@123" and type=="Employee":
            return render(request,"index.html",{"message":"Employee"})
        elif username=="Ravi" and password=="ravikumar@123" and type=="customer":
            return render(request,"index.html",{"message":"customer"})
        else:
            return render(request,"index.html",{"message":"error"})

    if request.method=="GET":
        return render(request,"index.html")
