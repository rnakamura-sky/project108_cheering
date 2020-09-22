from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.AccountLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]