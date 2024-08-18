from django.shortcuts import render,redirect
from core.models import *
from core.models import *
def home(request):
    datas=tasks.objects.all()
    context={'data':datas}
    if request.method == 'POST':
       task= request.POST.get('task')
       data=tasks.objects.create(taskname=task)
       data.save()
    return render(request,'Todolist.html',context)


def delete(request,id):
    data1=tasks.objects.get(id=id)
    sav=data1.delete()
    sav
    if sav:
        return redirect('homepage')
    return render(request,'Todolist.html')


def deleteall(request):
    data=tasks.objects.all()
    save=data.delete()
    save 
    if save:
      return redirect('homepage')
    return render(request,'Todolist.html')

     
def update(request, id):
    data=tasks.objects.get(id=id)
    context={'data':data}
    if request.method == 'POST':
        task=request.POST.get('Newtask')
        print(task)
        data.taskname=task
        data.save()
        return redirect('homepage')
    return render(request, 'Edit.html',context)
    