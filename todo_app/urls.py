
from django.urls import path
from . import views
app_name = 'todo_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('list/', views.list, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),

]