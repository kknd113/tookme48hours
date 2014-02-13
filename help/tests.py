from help.models import UsersModel
import unittest

class BackEndTest(unittest.TestCase):
    def setUp(self):
        UsersModel().TESTAPI_resetFixture()
        self.django = UsersModel(user='django', password='', count=1)
        self.iss = UsersModel(user='is', password='isit', count=1)
        self.fun = UsersModel(user='fun', password='yes', count=1)
        self.django.save()
        self.iss.save()
        self.fun.save()

    
    def reset(self):
        TESTAPI_resetFixture()







    def testlogIn1(self):
        self.assertEqual(2, UsersModel().login('django',''))
        self.assertEqual(3, UsersModel().login('django', ''))

    #def testlogIn2(self):
    #    self.assertEqual(3, login('django', ''))

    def testLogin3(self):
        self.assertEqual(-1, UsersModel().login('django', 'garbage'))
        
    def testLogin4(self):
        self.assertEqual(-1, UsersModel().login('django', '123'))
    
    def testLogin5(self):
        self.assertEqual(-1, UsersModel().login('is', ''))

    def testLogin6(self):
        self.assertEqual(2, UsersModel().login('is','isit'))

    def testAddUser1(self):
        self.assertEqual(1, UsersModel().add('adding','a_user'))

    def testAddUser2(self):
        self.assertEqual(-3, UsersModel().add('','emptyuserid'));

    def testAddUser3(self):
        self.assertEqual(-3, UsersModel().add('',''))

    def testAddUser4(self):
        self.assertEqual(-2, UsersModel().add('fun','duplicate'))

    def testAddUser5(self):
        self.assertEqual(-2, UsersModel().add('django', '340958340534850435'))

    def testAddUser6(self):
        self.assertEqual(-4, UsersModel().add('long','thisisalongpasswordthisisalongpasswordthisisalongpasswordthisisalongpasswordthisisalongpasswordthisisalongpasswordthisisalongpassword'))


    def testAddUser7(self):
        self.assertEqual(-3, UsersModel().add('longverylongusernamelongverylongusernamelongverylongusernamelongverylongusernamelongverylongusernamelongverylongusernamelongverylongusername', ''))

    def testReset1(self):
        self.assertEqual(1, UsersModel().TESTAPI_resetFixture())

    def testReset2(self):
        UsersModel().TESTAPI_resetFixture()
        self.assertEqual(-1,UsersModel().login('django',''))

    def testReset3(self):
        UsersModel().TESTAPI_resetFixture()
        self.assertEqual(1, UsersModel().add('django','newdjango'))
