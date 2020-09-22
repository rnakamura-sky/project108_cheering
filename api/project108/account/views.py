from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from .forms import LoginForm
from .models import User

# Create your views here.
class AccountLogin(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/request/')
        return render(request, 'account/login.html', {'form': form,})
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        return render(request, 'account/login.html', {'form': form,})