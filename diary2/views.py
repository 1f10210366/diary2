from django.shortcuts import render
from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    template_name = 'diary2/login.html'

def index(request):
    return render(request, 'index.html')
