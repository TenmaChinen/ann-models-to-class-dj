from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('convert/',views.convert,name='convert'),
]
