from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=10, unique=True, blank=False)
    password = models.CharField(max_length=50, blank=False)
    # ip1 = models.CharField(max_length=20, blank=True)
    # ip2 = models.CharField(max_length=20, blank=True)
    # ip3 = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    createdon = models.DateField(default=datetime.now().date())

class LiveIp(models.Model):
    username = models.CharField(max_length=10, unique=True, blank=False)
    ip = models.CharField(max_length=20)

class ClientLog(models.Model):
    username = models.CharField(max_length=10)
    date = models.DateField(default=datetime.now().date())
    login = models.TimeField(auto_now=True)
    logout = models.TimeField(default=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).time())
    ip = models.CharField(max_length=20, blank=True)

class Order(models.Model):
    username = models.CharField(max_length=10, blank=False)
    date = models.DateField(default=datetime.now().date())
    buytime = models.CharField(max_length=100, blank=True)
    buyprice = models.FloatField()
    instrument = models.CharField(max_length=50)
    qty = models.IntegerField()
    buy_status = models.CharField(max_length=50, blank=True)  
    buy_status_message = models.CharField(max_length=250, blank=True)    
    selltime = models.CharField(max_length=100, blank=True)
    sellprice = models.FloatField()
    sell_status = models.CharField(max_length=50, blank=True)  
    sell_status_message = models.CharField(max_length=250, blank=True)  
    diff = models.FloatField()
    profitloss = models.FloatField()


