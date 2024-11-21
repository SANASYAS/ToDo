from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.todo,name="todo"),
    path('todoadd/',views.add,name='todoadd'),
    path('delete/',views.delete,name='delete_all'),
    path('delete/<int:id>',views.delete,name='delete'),
]
