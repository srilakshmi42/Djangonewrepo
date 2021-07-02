from django.shortcuts import render

def showIndex(required):
    return render(required,"index.html")
