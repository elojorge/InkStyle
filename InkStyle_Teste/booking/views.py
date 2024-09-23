from django.shortcuts import render, redirect
from googleapiclient.discovery import build

#Função para criar um evento no Google Calendar
def create_google_calendar_event(credentials, event_data):
    # Constrói o serviço para a API do Google Calendar
    service = build('calendar', 'v3', credentials=credentials)

    # Cria o evento no calendário principal
    event = service.events().insert(calendarId='primary', body=event_data).execute()
    return event


def index(request):
    # logica para renderizar a página inicial 
    return render(request, 'booking/index.html')

def booking(request):
    # logica para renderizar a página inicial 
    return render(request, 'booking/booking.html')


#Create your views here.
def list_events(request):
    # Verifica se o usuário tem as credenciais na sessão
    credentials = request.session.get('credentials')
    if not credentials:
        return redirect('google_login')  # Redireciona para login se o usuário não estiver autenticado

#Constrói o serviço para a API do Google Calendar
    service = build('calendar', 'v3', credentials=credentials)

    # Busca os eventos do calendário principal
    events_result = service.events().list(calendarId='primary').execute()
    events = events_result.get('items', [])

    return render(request, 'events.html', {'events': events})


def create_event(request):
    # Verifica se o usuário tem as credenciais na sessão
    credentials = request.session.get('credentials')
    if not credentials:
        return redirect('google_login')

    if request.method == 'POST':
        # Coleta os dados do evento do formulário POST
        summary = request.POST.get('summary')
        description = request.POST.get('description')
        start_datetime = request.POST.get('start_datetime')
        end_datetime = request.POST.get('end_datetime')
        attendees = request.POST.getlist('attendees')

        # Define os dados do evento de forma dinâmica
        event_data = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'America/Sao_Paulo',
            },
            'attendees': [{'email': email} for email in attendees],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        # Chama a função para criar o evento
        event = create_google_calendar_event(credentials, event_data)

        # Redireciona para uma página de sucesso ou exibe a confirmação
        return render(request, 'event_created.html', {'event': event})

    return render(request, 'create_event.html')  # Exibe o formulário para criar o evento