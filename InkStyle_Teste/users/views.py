from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

#views.py

def index(request):
    return render(request, 'index.html')

def user(request):
    return render(request, 'user.html')



# class MinhaView(LoginRequiredMixin, View):
#  login_url = '/login/'

#  def get(self, request, *args, **kwargs):
#         return HttpResponse("Você está autenticado e acessou esta página!")