from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Todo


@csrf_exempt
def index(request):
    var = Todo.objects.all().order_by('-pub_date')
    return render(request, 'todoapp/index.html', {'var': var})


@csrf_exempt
def add_item(request):
    content = request.POST['content']
    car = Todo.objects.create(text=content) #comment---Todo(text=content) then car.save()
    return HttpResponseRedirect('/')

@csrf_exempt
def delete(request,id):
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect('/')
