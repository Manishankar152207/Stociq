from django.shortcuts import render
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from datetime import datetime
import json
# Create your views here.

@api_view(['GET','POST'])
def check_client(request):
    if request.method == 'POST':
        user = request.POST.get('username', '')
        passw = request.POST.get('password', '')
        ip = request.META['REMOTE_ADDR']
        if user and passw and ip:
            userdata = Client.objects.filter(username=user, password=passw).values()
            if len(userdata)==1:
                user_active = LiveIp.objects.filter(username=user, ip=ip).values()
                if len(user_active)>=1:
                    res = {'success':False}
                    json_data = JSONRenderer().render(res)
                else:                    
                    serializer = LiveIpSerializer(data = {"username":user, "ip":ip})
                    if serializer.is_valid():
                        serializer.save()
                    serializer = ClientLogSerializer(data={"username":user})
                    if serializer.is_valid():
                        serializer.save()
                    res = {'success':True}
                    json_data = JSONRenderer().render(res)
            else:
                res = {'success':False}
                json_data = JSONRenderer().render(res)
        else:
            res = {'success':False}
            json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    else:
        res = {'success':False}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        user = request.POST.get('username', '') 
        ke = request.POST.get('logout', False)       
        if user:
            try:
                userdata = LiveIp.objects.get(username=user)
                if userdata:                
                    userdata.delete() 
                    userlog = ClientLog.objects.get(username=user, date=datetime.now().time())
                    userlog.logout = str(datetime.now().time()) if not ke else ke
                    userlog.save()
                    res = {'success':True}
                    json_data = JSONRenderer().render(res)
            except:  
                res = {'success':False}
                json_data = JSONRenderer().render(res)                
        else:
            res = {'success':False}
            json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

    res = {'success':False}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['POST'])
def executed_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'success':True}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def live_ip(request):
    if request.method == 'POST':
        serializer = LiveIpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted', 'success':True}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_order(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

