from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self, request):
        return HttpResponse("<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>")


class SeznamView(View):
    def get(self, request):
        return HttpResponse("<h1>Vítejte v naší autopůjčovně!</h1>"
                            "<a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a> <br>"
                            "<h2>O naší autopůjčovně</h2>"
                            "<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>")

