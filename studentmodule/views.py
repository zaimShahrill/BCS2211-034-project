from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from studentmodule.models import Student, Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def index(request):
    
    return render(request,"index.html")

def newstudent(request):
    stumentor1=Student.objects.all().values()
    mymentor=Mentor.objects.all().values()

    if request.method=='POST':
        stuid=request.POST['stuid']
        stuname=request.POST['stuname']
        stuemail=request.POST['stuemail']
        stuage=request.POST['stuage']
        menid1=request.POST['selectmenid']
        mentornew = Mentor.objects.get(menid=menid1)
        data=Student(stuid=stuid, stuname=stuname,stuemail=stuemail, stuage=stuage, stumentor=mentornew)
        data.save()

        context={
        'stumentor':stumentor1,
        'mymentor':mymentor,
        'message': 'NEW STUDENT HAS BEEN SAVE'
        }
        
        return render(request,"newstudent.html",context)
    else:
        dict={
            'stumentor':stumentor1,
            'message': '',
            'mymentor':mymentor,
        }
    return render(request,"newstudent.html",dict)