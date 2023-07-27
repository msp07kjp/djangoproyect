from django.http import HttpResponse
from .models import Proyecto, Task
from django.shortcuts import render,get_object_or_404, redirect
from .forms import CreateNewTask, CreateNewProyect

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def proyect(request):
    proyects = list(Proyecto.objects.values())
    return render(request, 'proyects/proyect.html', {'proyects': proyects})
def task(request):
    #task= Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks= Task.objects.all()
    return render(request, 'tasks/task.html', {'tasks': tasks})
def create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            proyecto_id = 1
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            fecha_creacion = form.cleaned_data['fecha_creacion']
            fecha_entrega = form.cleaned_data['fecha_entrega']
            estado = form.cleaned_data['estado']
            hecho = form.cleaned_data['hecho']
            t = Task(proyecto_id=proyecto_id,nombre=nombre, descripcion=descripcion, fecha_creacion=fecha_creacion, fecha_entrega=fecha_entrega, estado=estado, hecho=hecho)
            t.save()
            return redirect('task')
    else:
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
        }
    )
def create_proyect(request):
    if request.method == 'POST':
        form = CreateNewProyect(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            fecha_creacion = form.cleaned_data['fecha_creacion']
            fecha_entrega = form.cleaned_data['fecha_entrega']
            estado = form.cleaned_data['estado']
            p = Proyecto(nombre=nombre, descripcion=descripcion, fecha_creacion=fecha_creacion, fecha_entrega=fecha_entrega, estado=estado)
            p.save()
            return redirect('proyect')
    else:
        return render(request, 'proyects/create_proyectos.html', {
        'form': CreateNewProyect()
        }
    )
def proyect_detail(request, id):
    proyect = get_object_or_404(Proyecto, id=id)
    tasks = Task.objects.filter(proyecto_id=id)
    return render(request, 'proyects/proyect_detail.html', {
        'proyect': proyect,
        'tasks': tasks
        }
    )
def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def hello(request,username):
    return HttpResponse("<h1>hello desde Django %s</h1>" % username)