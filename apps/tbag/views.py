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
        webhook = SyncWebhook.from_url("")
        resp =webhook.send(f'Days to Bangalore Trip V4 : **{dat.days}**')
        return HttpResponse(resp)
