from django.shortcuts import render
from django.http import HttpResponse

def page_not_found(request):
	return render(request, '404.html')

def server_error(request):
	return HttpResponse('抱歉，服务器内部错误！')