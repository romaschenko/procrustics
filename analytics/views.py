from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse 

from .models import Analysis, Rating, Alert

# Create your views here.

class Home(ListView):
    model = Analysis
    template_name = 'analytics/index.html'
    context_object_name ='posts'
    paginate_by = 5



class GetAnalysis(DetailView):
    model = Analysis
    template_name = 'analytics/single.html'
    context_object_name = 'analysis'

#def Analyses(request):
 #   return HttpResponse ('<h1>Привет!</h1>')

class Analyses(ListView):
    model = Analysis
    template_name = 'analytics/analyses.html'
    context_object_name ='posts'
    paginate_by = 10


#def sidebar_filler(request):
  #  markets= Market.objects.all()
    
 #   return render (request,template_name= "analytics/markets.html", markets = markets )


class PostsByMarket(ListView):

    template_name = 'analytics/analyses.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 10

    #def get_context_data(self,*,object_list=None, **kwargs):
       # context = super().get_context_data(**kwargs)
       # context['title'] = self.get_upper(Market.objects.get(symbol=self.kwargs['symbol.market_slug']))
       # return context

    def get_queryset(self):
        #return Analysis.objects.filter('symbol.market.slug'==self.kwargs['slug']) #,is_published=True).select_related('market')
        return Analysis.objects.filter(symbol__market__slug=self.kwargs['slug'])


def contacts(request):
    return render(request,'analytics/contact.html',{'content':"hello world!",})

def about(request):
    return render(request,'analytics/about.html',{'content':"hello world!",})

def prices(request):
    return render(request,'analytics/prices.html',{'content':"hello world!",})

def tokens(request):

    return render(request,'analytics/tokens.html',{'content':"hello world!",})

def trust(request):

    return render(request,'analytics/trust.html',{'content':"hello world!",})

def rating(request):
    return render(request,'analytics/rating.html',{'content':"hello world!",})


class Get_Rating(ListView):
    model = Rating 
    template_name = 'analytics/rating.html'
    context_object_name ='posts'
    paginate_by = 10


class Get_Alerts(ListView):
    model = Alert
    template_name = 'analytics/stats.html'
    context_object_name ='posts'

    def win_counter(self):
        wins = Alert.objects.all().count
        return wins
    #paginate_by = 10


