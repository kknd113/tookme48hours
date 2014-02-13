from django.db import models
import json

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128






# Create your models here.
class UsersModel(models.Model):
	user = models.CharField(max_length = MAX_USERNAME_LENGTH)
	password = models.CharField(max_length = MAX_PASSWORD_LENGTH)
	count = models.IntegerField()

	def __unicode__(self):
		return self.user + ", " + self.password

	def login(self, usr, pw):
		acct = UsersModel.objects.filter(user__exact=usr)
		if not acct or acct[0].password!=pw:
			return ERR_BAD_CREDENTIALS
		else:
			acct[0].count+=1
			acct[0].save()
			return acct[0].count


	def add(self, usr, pw):
		if len(usr) < 1 or len(usr) > 128:
			return ERR_BAD_USERNAME
		elif UsersModel.objects.filter(user__exact=usr).exists():
			return ERR_USER_EXISTS
		elif len(pw) > 128:
			return ERR_BAD_PASSWORD
		else:
			acct = UsersModel(user=usr, password=pw,count=1)
			acct.save()
			return acct.count

	def TESTAPI_resetFixture(self):
		UsersModel.objects.all().delete()
		return SUCCESS

	def TESTAPI_unitTests(self):
		return SUCCESS