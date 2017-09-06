from django.conf.urls import url
from comments import views

app_name = 'comments'
urlpatterns = [
	url(r'^comment/food/(?P<food_pk>\d+)/$', views.comment, name='comment') 
]