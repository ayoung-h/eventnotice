from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def upload_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_thanks')
    else:
        form = EventForm()
        
    return render(request, 'events/upload_event.html', {'form': form})

def event_thanks(request):
    return render(request, 'events/event_thanks.html')

def approved_events(request):
    events = Event.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'events/approved_events.html', {'events': events})

def home(request):
    return render(request, 'events/home.html')