from django.shortcuts import render
import requests


class exchange():
    def __init__(self):
        self.api_url= 'https://v6.exchangerate-api.com/v6/'
        self.api_key= '70317810c3cf45a29226439d'

    def get_exchange_usd(self):
        response=requests.get(f'{self.api_url}/{self.api_key}/latest/USD')
        return response.json()
    
    def get_exchange_azn(self):
        response=requests.get(f'{self.api_url}/{self.api_key}/latest/AZN')
        return response.json()

    def get_exchange_eur(self):
        response=requests.get(f'{self.api_url}/{self.api_key}/latest/EUR')
        return response.json()

exchange1=exchange()
usd1=exchange1.get_exchange_usd()
azn1=exchange1.get_exchange_azn()
eur1=exchange1.get_exchange_eur()





def index(request):
    context=None
    if  request.method=='POST':
        first=request.POST['first']
        last=request.POST['last']
        money=request.POST['money']
        if first and last and money:
            if first=='usd' and last=='azn':
                usd=usd1['conversion_rates']['AZN']
                usd=float(usd)*float(money)
                context={
                    'data':usd
                }
            elif first=='usd' and last=='eur':
                eur=usd1['conversion_rates']['EUR']
                eur=float(eur)*float(money)
                context={
                    'data':eur
                } 
            elif first=='azn' and last=='usd':
                azn=azn1['conversion_rates']['USD']
                azn=float(azn)*float(money)
                context={
                    'data':azn
                }
            elif first=='azn' and last=='eur':
                azn=azn1['conversion_rates']['EUR']
                azn=float(azn)*float(money)
                context={
                    'data':azn
                } 
            elif first=='eur' and last=='usd':
                eur=eur1['conversion_rates']['USD']
                eur=float(eur)*float(money)
                context={
                    'data':eur
                } 
            elif first=='eur' and last=='azn':
                eur=eur1['conversion_rates']['AZN']
                eur=float(eur)*float(money)
                context={
                    'data':eur
                } 
            
    return render(request,"index.html",context=context)