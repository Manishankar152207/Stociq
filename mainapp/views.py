from django.shortcuts import render
from api.models import *
from api.serializers import *
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse
import json
# Create your views here.
def login(request):
    return render(request, "login.html")


def index(request):
    today_trade = Order.objects.filter(date=datetime.now().date()).order_by('-profitloss').values()
    today_earning = Order.objects.filter(date=datetime.now().date()).aggregate(Sum('profitloss'))
    total_earning = Order.objects.filter().aggregate(Sum('profitloss'))
    total_client = len(Client.objects.all())
    top_gainer_client = []
    for trade in today_trade:
        client = Client.objects.filter(username=trade["username"]).values()[0]
        top_gainer_client.append(client)
    return render(request, "index.html", context={"total_client":total_client, "total_earning": total_earning, "today_earning":today_earning, "top_gainer":top_gainer_client, "today_trade":today_trade})


def clients(request):
    if request.method == "GET":
        changestatus = request.GET.get("changestatus", False)
        getclienttrades = request.GET.get("getclienttrades", False)
        if not changestatus and not getclienttrades:
            clients = Client.objects.all().values()
            total_client = len(clients) 
            active_client = len(Client.objects.filter(status=True))
            block_client = total_client - active_client
            return render(request, "clients.html", context={"total_client":total_client, "block_client":block_client, "active_client":active_client, "clients":clients})
        
        elif not changestatus and getclienttrades:
            if not request.GET.get("show", False):
                clienttrades = Order.objects.filter(username=getclienttrades)
                # return render(request, "clientstrade.html", context={"today_trade":clienttrades, "clienttrade":getclienttrades})
            else:
                clienttrades = Order.objects.filter(username=getclienttrades, date=datetime.now().date())
            return render(request, "clientstrade.html", context={"today_trade":clienttrades, "clienttrade":getclienttrades})
        else:
            user_exist = Client.objects.filter(username=changestatus).exists()
            if user_exist:
                user = Client.objects.get(username=changestatus)
                user.status = not user.status
                user.save()
                return HttpResponse(json.dumps({'success':True}), content_type='application/json') 
            return HttpResponse(json.dumps({'success':False}), content_type='application/json') 

    elif request.method == "POST":
        username = Client.objects.filter(username=request.POST["username"]).exists()
        if not username:
            serializer = ClientSerializer(data = request.POST)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Inserted', 'success':True}
                return HttpResponse(json.dumps(res), content_type='application/json')
        return HttpResponse(json.dumps({"msg":"Client already exist.", 'success':False}), content_type='application/json')


def alltrades(request):
    total_trade = Order.objects.all()
    total_earning = Order.objects.filter().aggregate(Sum('profitloss'))
    today_trade = Order.objects.filter(date=datetime.now().date()).order_by('-profitloss').values()    
    today_earning = Order.objects.filter(date=datetime.now().date()).aggregate(Sum('profitloss'))
    return render(request, "alltrades.html", context={"total_trade":len(total_trade), "total_earning":total_earning, "today_trade":len(today_trade), "today_earning":today_earning, "all_trade":total_trade})

def todaytrades(request):
    today_trade = Order.objects.filter(date=datetime.now().date()).order_by('-profitloss').values()    
    today_earning = Order.objects.filter(date=datetime.now().date()).aggregate(Sum('profitloss'))
    return render(request, "todaytrades.html", context={"today_trade_len":len(today_trade), "today_earning":today_earning, "today_trade":today_trade})

def clientlogs(request):
    if request.method == 'GET':
        show = request.GET.get("show", False)
        if not show:
            logs = ClientLog.objects.all()
            return render(request, "clientlogs.html", context={"total_logs":len(logs), "logs":logs})
        else:
            logs = ClientLog.objects.filter(date=datetime.now().date()).values()
            print(logs)
            return render(request, "clientlogs.html", context={"total_logs":len(logs), "logs":logs})

def adminusers(request):
    return render(request, "adminuser.html")