from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Task
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return HttpResponse("index desde Django")
def hello(request,username):
    return HttpResponse("<h1>hello desde Django %s</h1>" % username)
def about(request):
    return HttpResponse("about")
def proyect(request):
    proyects = list(Proyecto.objects.values())
    return JsonResponse(proyects, safe=False)
def task(request,id):
    #task= Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task: %s" % task.nombre)