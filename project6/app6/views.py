from django.shortcuts import render

def showIndex(request):
    student_info={"data":
                    [
                        {"idno":101,"name":"Goutham","marks":[91,83,65,87,74,99]},
                        {"idno":102,"name":"Gouthami","marks":[90,80,65,81,74,76]},
                        {"idno":103,"name":"Srivani","marks":[89,'A',69,83,54,39]},
                        {"idno":104,"name":"Sri","marks":[61,73,95,47,79,79]},
                        {"idno":105,"name":"Arjun","marks":[81,85,69,82,74,59]}
                    ]

                }
    return render(request,"index.html",student_info)
