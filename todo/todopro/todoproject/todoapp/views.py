from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .form import TodoForm
from .models import task
from django.views.generic import ListView, UpdateView, DeleteView

# Create your views here.
class todoListview(ListView):
    model=task
    template_name = 'index.html'
    context_object_name = 'task'
class tododetail(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'tk'
class todoup(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'tk'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cv',kwargs={'pk':self.object.id})
class tododelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbv')

def todo(request):
    tasks1 = task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        date=request.POST.get('date','')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()

    return render(request,"index.html",{'task':tasks1})
def delete(request,tkid):
    taskid=task.objects.get(id=tkid)
    if request.method =="POST":
        taskid.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,fmid):
    fid=task.objects.get(id=fmid)
    fm=TodoForm(request.POST or None, instance=fid)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    return render(request,'edit.html',{'fm':fm,"tk":fid})
