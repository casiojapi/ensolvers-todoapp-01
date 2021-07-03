from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="list"),
    path('edit/<str:primaryKey>', views.edit_task, name="edit"),
    path('delete/<str:primaryKey>', views.delete_task, name="delete"),
    path('check/<str:primaryKey>', views.update_task_completion, name="check"),
]