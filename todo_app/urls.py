from django.urls import path
from . import views

urlpatterns = [
		path('', views.index, name="todos"),
		path('insert_todo/', views.insert_item, name='insert_todo'),
		path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo')
]