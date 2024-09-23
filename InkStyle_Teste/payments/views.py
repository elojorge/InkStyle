from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'payments/index.html')

def payments(request):

    return render(request, 'payments/payments.html')
