from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.core import serializers
from .models import Todo

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'index.html'


def AllTodo(request):
  todos = Todo.objects.all()
  data = serializers.serialize('json', todos)

  return HttpResponse(data, content_type='application/json')


def SingleTodo(request, todo_id):
  todos = Todo.objects.get(pk=todo_id)
  print("todo", todos)
  data = serializers.serialize('json', [todos,])

  return HttpResponse(data, content_type='application/json')


