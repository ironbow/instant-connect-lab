from django.shortcuts import render
from .models import Device
from .forms import MeetingForm, DeviceForm, ControlHubForm
import requests
import json

def home(request):

    devices = Device.objects.all()
    context = {}
    context["devices"] = devices
    context['form'] = MeetingForm()
    return render(request, "home.html", context)

def add_device(request):
    context = {}
    form = DeviceForm(request.POST or None, request.FILES or None)
    print(request)
    if form.is_valid():
        form.save()
        form = DeviceForm()
    context['form'] = form
    return render(request, "add_device.html", context)

def add_controlhub(request):
    context = {}
    form = ControlHubForm(request.POST or None, request.FILES or None)
    print(request)
    if form.is_valid():
        form.save()
        form = ControlHubForm()
    context['form'] = form
    return render(request, "add_controlhub.html", context)

def meeting(request):
    subject = request.POST['subject']
    sip_uri = request.POST['sip_uri']
    num_guests = request.POST['guests']
    num_hosts = request.POST['hosts']
    bot_token = request.POST['bot_token']
    vertical = request.POST['vertical']
    host_login = request.POST.get('host_login_required', False)
    if host_login == "on":
        host_login = True
    url = "https://mtg-broker-a.wbx2.com/api/v2/joseencrypt"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bot_token}"
    }
    payload = {
        "jwt": {
            "sub": subject,
            "flow": {
                "id": "sip-no-knock",
                "data": [
                    {
                        "uri": sip_uri
                    }
                ]
            }
    },
    "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
    "provideShortUrls": True,
    "verticalType": vertical,
    "loginUrlForHost": host_login,
    "numGuest": num_guests,
    "numHost": num_hosts
    }
    meeting = requests.post(url, headers=headers, json=payload).json()
    hosts = []
    guests = []
    for host in meeting['host']:
        print(host)
        hosts.append(f"{meeting['baseUrl']}{host['short']}")
    for guest in meeting['guest']:
        print(guest)
        guests.append(f"{meeting['baseUrl']}{guest['short']}")
    
    context = {
        "meeting": {
            "hosts": hosts,
            "guests": guests
        }
    }
   
    return render(request, "meeting.html", context)
