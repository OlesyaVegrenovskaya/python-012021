from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request):
        return("Zde bude titulní stránka.")

class SeznamView(View):
    def get(self, request):
        return("Zde bude seznam aut.")


# Create your views here.
