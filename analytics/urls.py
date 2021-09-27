from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('analysis/<str:slug>/', GetAnalysis.as_view(), name='analysis'),
    path('analyses/', Analyses.as_view(), name='analyses'),

    #path('market, Market.as_view')
    path('market/<str:slug>/', PostsByMarket.as_view(),name='market'),
    #path('tag/<str:slug>/', PostsByTag.as_view(),name='tag'),
    #path('post/<str:slug>/', GetPost.as_view(), name='post'),
    #path('search/', Search.as_view(), name='search'),
    path('contact/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('prices/', prices, name='prices'),
    path('tokens/', tokens, name='tokens'),
    path('trust/', trust, name='trust'),
    path('rating/', Get_Rating.as_view() , name='rating'),
    path('stats/', Get_Alerts.as_view() , name='stats'),

]   