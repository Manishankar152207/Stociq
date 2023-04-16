from rest_framework import serializers
from api.models import Client, LiveIp, Order, ClientLog

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["username", "password"]

class LiveIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveIp
        fields = ["username", "ip"]

class ClientLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLog
        fields = ["username", "ip", "date", "login"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["username","date", "buytime", "buyprice", "instrument", "qty", "buy_status", "buy_status_message", "selltime","sellprice", "sell_status", "sell_status_message","diff", "profitloss"]
