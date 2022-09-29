from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
import requests
from django.http import HttpResponse
from discord import SyncWebhook
import datetime
from dateutil import relativedelta
from datetime import date
# Create your views here.
class Hook(APIView):
    def get(self,request):
        dat =date(2022,12,17)- date.today()
        webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1012756464504422400/NWAbxPwpRF8uuHTpLFTm0UlK5vFQBWTc2zFNTrZAjPusieKlO8rE4qQPrAq0w9ksUm1e")
        resp =webhook.send(f'Sleeps to Bangalore Trip V4 : **{dat.days}**')
        return HttpResponse(resp)
