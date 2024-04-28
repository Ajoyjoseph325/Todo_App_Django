from django.shortcuts import render,redirect
from . forms import Todoforms



from . models import task

def tasklist(request):
    obj=task.objects.all()
    return render(request,"tasklist.html",{'tasks':obj})
    

    
def tasks(request):
    if request.method=='POST':
        taskname=request.POST.get('tname')
        prio=request.POST.get('priority')
        date=request.POST.get('date')
        obj=task(name=taskname,priority=prio,date=date)
        obj.save()
        return redirect('/')


    return render(request,"tasks.html")
def deltask(request,id):
    obj=task.objects.get(id=id)
    obj.delete()
    return redirect('/')
def update(request,id):
    uptask=task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=uptask)
    # obj=shop.objects.get(id=id)
    # form=modeform(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})

    


    
    # Create your views here.
