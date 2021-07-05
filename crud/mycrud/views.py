from django.contrib.admin.decorators import register
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import EmployeeRegistration
from .models import User
# Create your views here.
def form_data(request):
    if request.method=='POST':
        fm=EmployeeRegistration(request.POST)
        if fm.is_valid():
         fm.save()
         fm=EmployeeRegistration()
    else:
         fm=EmployeeRegistration()
    stu=User.objects.all()
    return render(request,'mycrud/forms.html',{'form':fm,'stu':stu})
def add_show(request):
    if request.method=='POST':
        fm=EmployeeRegistration(request.POST)
        if fm.is_valid():
         fm.save()
         fm=EmployeeRegistration()
    else:
         fm=EmployeeRegistration()
    stu=User.objects.all()
    return render(request,'mycrud/show.html',{'form':fm,'stu':stu})


def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=EmployeeRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=EmployeeRegistration(instance=pi)
    return render(request,'mycrud/update.html',{'form':fm})