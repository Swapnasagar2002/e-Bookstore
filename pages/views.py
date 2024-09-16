from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
   # return HttpResponse("<h1>Hello World</h1>")
   return render(request,'pages/index.html')
def aboutus(request):
    # return HttpResponse("<h2>About Us</h2>")
    name = " Jhon"
    student =  {1:"Sidd", 2:"Subu", 3:"Raja", 4:"Nana"}
    results = {
        1 : {"name" : "Sidd", "cgpa" : [9.2,9.4,9.6,9.8]},
        2 : {"name" : "Raja", "cgpa" : [9.0,8.4,9.9,9.2]},
        3 : {"name" : "Subu", "cgpa" : [10.0,10.0,10.0,10.0]},
        4 : {"name" : "Nana", "cgpa" : [9.2,9.2,9.2,9.8]}
        }
    context = {
        "name" : "Sidd",
        "age" : 20,
        "num1" : 12,
        "num2" : 20,
        "numl" : [1,2,3,4,5,6],
        "students" : student,
        "result" : results
    }
    return render(request,'pages/about.html',context)
