from django.urls import path
from . import views

app_name = 'cheering'
urlpatterns = [
    path('request/', views.index, name='index'),
    path('request/call/', views.call, name='call'),
]
