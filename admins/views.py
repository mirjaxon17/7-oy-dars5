from django.shortcuts import render
from .models import Admins,Adres
from django.views import View

class AdminViews(View):
    def get(self,request):
        admins = Admins.objects.all()
        return render(request,'admins.html',{'admins':admins})



class AdresViews(View):
    def get(self,request):
        adres = Adres.objects.all()
        return render(request,'adress.html',{'adres':adres})


