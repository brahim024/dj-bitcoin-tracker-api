from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def price(request):
    url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data=requests.get(url).json()
    return HttpResponse(data)
    #return render(request,'price/prices.html',{'data':data})

