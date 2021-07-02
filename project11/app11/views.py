from django.shortcuts import render

def showIndex(request):
    data={"name":"srivani","salary":185000.00}
    return render(request,"index.html",data)
