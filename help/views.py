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



@csrf_exempt        
def resetFixture(request):
	response = UsersModel().TESTAPI_resetFixture()
	if (response == SUCCESS):
		return HttpResponse(json.dumps({"errCode" : SUCCESS}), content_type = "application/json")

@csrf_exempt        
def unitTests(request):
    buffer = StringIO.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(BackEndTest)
    result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)


    rv = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
    return HttpResponse(json.dumps(rv), content_type = "application/json")