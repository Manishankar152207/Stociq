from django.contrib import admin
from api.models import Client, LiveIp, Order, ClientLog

# Register your models here.
@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['id','username','password', 'status','createdon']

@admin.register(LiveIp)
class LiveIpAdmin(admin.ModelAdmin):
    list_display = ['username','ip']

@admin.register(ClientLog)
class ClientLogAdmin(admin.ModelAdmin):
    list_display = ['username', 'ip', 'date', 'login', 'logout']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['username','date','buytime','buyprice','instrument','qty', 'buy_status', 'buy_status_message', 'selltime','sellprice', 'sell_status', 'sell_status_message','diff', 'profitloss']

