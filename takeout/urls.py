from django.conf.urls import url
from takeout import views

app_name = 'takeout'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^menu/(?P<menu_name>\w+)/$', views.menu, name='menu'),
	url(r'^food/(?P<food_name>\w+)/$', views.food, name='food'),
	url(r'^search/$', views.search, name='search'),
	url(r'^more/(?P<menu_name>\w+)/$', views.more, name='more')
]
