from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse, HttpRequest

def index(request):
	context = Todo.objects.all();
	return render(request, 'todo_app/todo_list.html', {'todos': context})

def insert_item(request):	
	todo = Todo(content = request.POST['content'])		
	todo.save()
	return redirect('/todos')

def delete_todo(request, todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.delete()
	return redirect('/todos')


	
