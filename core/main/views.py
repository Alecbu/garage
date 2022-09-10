from django.shortcuts import render
from django.views.generic import ListView
from .models import Menu, Home, HomeIntro, HomeServ1, HomeServ2, HomeServ3

# Create your views here.

class MenuListView(ListView):
    template_name = 'basefooter.html'

    def get (self, request):  
        return render(request, self.template_name)

class HomeListView(ListView):
    template_name = 'index.html'

    def get (self, request):   
        homes = Home.objects.all()
        homeintros = HomeIntro.objects.all()
        homeserv1s = HomeServ1.objects.all()
        homeserv2s = HomeServ2.objects.all()
        homeserv3s = HomeServ3.objects.all()
        return render(request, self.template_name, {
            'homes' : homes, 'homeintros' : homeintros,
            'homeserv1s' : homeserv1s, 'homeserv2s' : homeserv2s,
            'homeserv3s' : homeserv3s,
        })



