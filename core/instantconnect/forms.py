from django import forms
from .models import Device, ControlHub

class MeetingForm(forms.Form):
    subject = forms.CharField(max_length=20)
    vertical = forms.ChoiceField(choices=(("hc", "HealthCare"), ("gen", "General")))
    hosts = forms.ChoiceField(choices=((int(x), x) for x in range(1,26)))
    guests = forms.ChoiceField(choices=((int(x), x) for x in range(1,26)))
    host_login_required = forms.BooleanField(initial=True, required=False)

class DeviceForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    sip_uri = forms.CharField(max_length=200)
    control_hub = forms.ModelChoiceField(queryset=ControlHub.objects.all())

    class Meta:
        model = Device
        fields = "__all__"

class ControlHubForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    bot_token = forms.CharField(max_length=300)

    class Meta:
        model = ControlHub
        fields = "__all__"
    
