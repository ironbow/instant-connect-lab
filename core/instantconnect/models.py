from django.db import models


class ControlHub(models.Model):
     name = models.CharField(max_length=30)
     bot_token = models.CharField(max_length=300)

     def __str__(self): 
         return self.name

class Device(models.Model):
    name = models.CharField(max_length=30)
    sip_uri = models.CharField(max_length=200)
    control_hub = models.ForeignKey(ControlHub, on_delete=models.CASCADE)

    def __str__(self): 
         return self.name

    

