from django.shortcuts import render
from django.views import View

# Create your views here.
class Hook(View):
    print('hook hit')
