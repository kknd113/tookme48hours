from django.shortcuts import render
from django.http import HttpResponse
from models import UsersModel

# Create your views here.
def mainView(request):
	return HttpResponse("hi")