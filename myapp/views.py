from django.http import HttpResponse
from .models import Proyecto, Task
from django.shortcuts import render,get_object_or_404
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def proyect(request):
    proyects = list(Proyecto.objects.values())
    return render(request, 'proyect.html', {'proyects': proyects})
def task(request):
    #task= Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    return render(request, 'task.html')
def hello(request,username):
    return HttpResponse("<h1>hello desde Django %s</h1>" % username)