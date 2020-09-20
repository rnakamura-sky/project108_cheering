from django.urls import path

from . import views

app_name  = 'raspberry'
urlpatterns = [
    path('run/', views.run, name='run')
]
