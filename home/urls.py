from django.urls import path
from .views import *
urlpatterns=[
	path('', HomePageView, name='home'),
	path('about/', AboutPageView, name='about'),
	path('news/', NewsPageView, name='news'),

	path('contact/', ContactPageView, name='contact'),
	path('galarey/', GalareyPageView, name='galarey'),
	path('<slug:slug>/', NewsDetailView, name='news_detail'),



]