from django.urls import path, include
from . import views
 
urlpatterns = [
   path('', views.index, name="index"),
   path('logout/', views.logout, name="logout"),
   path('create_table/', views.CreateTable, name="create_table"),
   path('create_column/<int:t_id>/', views.CreateColumn, name="create_column"),
]