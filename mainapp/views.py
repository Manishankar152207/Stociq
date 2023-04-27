from django.shortcuts import render, redirect
from api.models import *
from api.serializers import *
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse
import json
from mainapp.forms import NewUserForm
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("index")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
        return render(request, "login.html")

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if not User.objects.filter(username = request.POST['username']):
                if request.POST['password1'] == request.POST['password2']:
                    form = NewUserForm(request.POST)
                    if form.is_valid():
                        user = form.save()
                        messages.success(request, "Registration successful." )
                        return redirect("login")
                    messages.error(request, "Unsuccessful registration. Invalid information.")
                else:
                    messages.error(request, "The two password fields doesn't match.")
            else:
                messages.error(request, "Username already exist.")
        return render(request, "register.html")
    return redirect("index")

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.info(request, "You have successfully logged out.") 
    return redirect("login")

def index(request):
    if request.user.is_authenticated:
        today_trade = Order.objects.filter(date=datetime.now().date()).order_by('-profitloss').values()
        today_earning = Order.objects.filter(date=datetime.now().date()).aggregate(Sum('profitloss'))
        total_earning = Order.objects.filter().aggregate(Sum('profitloss'))
        total_client = len(Client.objects.all())
        top_gainer_client = []
        for trade in today_trade:
            client = Client.objects.filter(username=trade["username"]).values()[0]
            top_gainer_client.append(client)
        return render(request, "index.html", context={"total_client":total_client, "total_earning": total_earning, "today_earning":today_earning, "top_gainer":top_gainer_client, "today_trade":today_trade})
    else:
        return redirect("login")

def clients(request):
    if request.user.is_authenticated:
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
    else:
        return redirect("login")
    
def alltrades(request):
    if request.user.is_authenticated:
        total_trade = Order.objects.all()
        total_earning = Order.objects.filter().aggregate(Sum('profitloss'))
        today_trade = Order.objects.filter(date=datetime.now().date()).order_by('-profitloss').values()    
        today_earning = Order.objects.filter(date=datetime.now().date()).aggregate(Sum('profitloss'))
        return render(request, "alltrades.html", context={"total_trade":len(total_trade), "total_earning":total_earning, "today_trade":len(today_trade), "today_earning":today_earning, "all_trade":total_trade})
    else:
        return redirect("login")
    
def todaytrades(request):
    if request.user.is_authenticated:
        today_trade = Order.objects.filter(date=datetime.now().date()).order_by('-profitloss').values()    
        today_earning = Order.objects.filter(date=datetime.now().date()).aggregate(Sum('profitloss'))
        return render(request, "todaytrades.html", context={"today_trade_len":len(today_trade), "today_earning":today_earning, "today_trade":today_trade})
    else:
        return redirect("login")
    
def clientlogs(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            show = request.GET.get("show", False)
            if not show:
                logs = ClientLog.objects.all()
                return render(request, "clientlogs.html", context={"total_logs":len(logs), "logs":logs})
            else:
                logs = ClientLog.objects.filter(date=datetime.now().date()).values()
                print(logs)
                return render(request, "clientlogs.html", context={"total_logs":len(logs), "logs":logs})
    else:
        return redirect("login")
    
