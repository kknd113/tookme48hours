from django.shortcuts import render
from django.http import HttpResponse
from models import UsersModel
from tests import *
import unittest
import StringIO
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json


SUCCESS = 1  

# Create your views here.
@csrf_exempt
def mainView(request):
	return render_to_response('client.html')



@csrf_exempt
def loginView(request):
	print "loginview"
	try:
		req = json.loads(request.body)
		usr = req["user"]
		pw = req["password"]
	except:
		return request.send_error(500)
	response = UsersModel().login(usr, pw)
	if response < 0:
		return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")
	else:
		return HttpResponse(json.dumps({"errCode": SUCCESS, "count": response}), content_type = "application/json")




@csrf_exempt
def addView(request):
	try:
		req = json.loads(request.body)
		usr = req["user"]
		pw = req["password"]
	except:
		return request.send_error(500)


	response = UsersModel().add(usr,pw)
	if response < 0:
		return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")
	else:
		return HttpResponse(json.dumps({"errCode": SUCCESS, "count": response}), content_type = "application/json")