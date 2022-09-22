from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
    path('index',views.index,name='index'),
]
