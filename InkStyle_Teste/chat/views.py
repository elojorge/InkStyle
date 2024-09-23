from django.shortcuts import render

#defina a view chamada 'chat'
def chat(request):
    # logica para renderizar a página de chat
    return render(request, 'chat/chat.html')

#defina a view chamada 'index'
def index(request):
    # logica para renderizar a página inicial do chat
    return render(request, 'chat/index.html')