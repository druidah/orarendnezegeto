from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ICSLink
from .forms import ICSUrlForm
from django.contrib.auth import login
from .forms import UserRegistrationForm
from icalendar import Calendar
import requests
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import datetime
from django.utils.timezone import now
from django.contrib.auth.views import LogoutView

@login_required  
def ics_link_detail(request, pk):
    ics_link = get_object_or_404(ICSLink, pk=pk, user=request.user)
    response = requests.get(ics_link.url)
    calendar = Calendar.from_ical(response.content)

    events = []
    current_date = now()  
    current_week_start = current_date - datetime.timedelta(days=current_date.weekday())  # Hétfő datetime típussal
    current_week_end = current_week_start + datetime.timedelta(days=6)  # Vasárnap datetime típussal

    # Beállítjuk 0:00-ra (éjfélre)
    current_week_start = current_week_start.replace(hour=0, minute=0, second=0, microsecond=0)
    current_week_end = current_week_end.replace(hour=23, minute=59, second=59, microsecond=999999)

    for component in calendar.walk():
        if component.name == "VEVENT":
            event_start = component.get('dtstart').dt
            event_end = component.get('dtend').dt
            
            # Ellenőrizzük, hogy az esemény a jelenlegi hétre esik-e
            if isinstance(event_start, datetime.datetime):
                pass  # Az esemény már datetime

            elif isinstance(event_start, datetime.date):
                event_start = datetime.datetime.combine(event_start, datetime.time.min)  # Konvertáljuk datetime-ba

            if isinstance(event_end, datetime.datetime):
                pass  # Az esemény már datetime

            elif isinstance(event_end, datetime.date):
                event_end = datetime.datetime.combine(event_end, datetime.time.min)  # Konvertáljuk datetime-ba

            # Most már lehet összehasonlítani
            if current_week_start <= event_start <= current_week_end:
                event = {
                    'summary': component.get('summary'),
                    'start_time': event_start,
                    'end_time': event_end,
                    'location': component.get('location', 'Nincs helyszín megadva')
                }
                events.append(event)

    # Események rendezése az időpontjuk szerint
    events.sort(key=lambda x: x['start_time'])

    return render(request, 'orarend.html', {'events': events})

def user_links(request):
    
    user_links = ICSLink.objects.filter(user=request.user)

    # Form kezelés
    if request.method == 'POST':
        form = ICSUrlForm(request.POST)
        if form.is_valid():
            ics_url = form.cleaned_data['ics_url']
            # Új ICS URL mentése az aktuális felhasználóhoz
            ICSLink.objects.create(user=request.user, url=ics_url)
            return redirect('user_links')  # Visszairányítás a saját linkek oldalára
    else:
        form = ICSUrlForm()


    return render(request, 'felhasznalolinkje.html', {'form': form, 'user_links': user_links})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('user_links')  
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
def index(request):
    return render(request, 'index.html')
