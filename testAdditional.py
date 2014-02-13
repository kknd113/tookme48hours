"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib
        
class TestAddUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAddUser1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'django', 'password' : 'pw'} )
        self.assertResponse(respData, count = 1)

    def testAddUser2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'dup', 'password' : 'dup'} )
        respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'dup', 'password' : 'dup'} )
        self.assertResponse(respData2, count = None, errCode = -2)

    def testAddUser4(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'aaa', 'password' : 'aaa'} )
        respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'aaa', 'password' : 'bbb'} )
        self.assertResponse(respData2, count = None, errCode = -2)


    def test_Adding5(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'emptyuser'} )
        self.assertResponse(respData, count = None, errCode = -3)


    def test_Adding6(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'longlonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusername', 'password' : 'lol'} )
        self.assertResponse(respData, count = None, errCode = -3)

    def test_Adding7(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'longlonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusernamelonglonglongusername', 'password' : ''} )
        self.assertResponse(respData, count = None, errCode = -3)

    def test_Adding8(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'longpw', 'password' : 'longpasswordislongverylonglongpasswordislongverylonglongpasswordislongverylonglongpasswordislongverylonglongpasswordislongverylonglongpasswordislongverylonglongpasswordislongverylonglongpasswordislongverylong'} )
        self.assertResponse(respData, count = None, errCode = -4)

    def test_Adding9(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : ''} )
        self.assertResponse(respData, count = None, errCode = -3)



class TestLogin(testLib.RestTestCase):
    """Test logging in users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)



    def test_loggingIn1(self):
        respDataprev = self.makeRequest("/users/add", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        self.assertResponse(respData, count = 2)

    def test_loggingIn2(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData1 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData3 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        self.assertResponse(respData3, count = 4)


    def test_loggingIn3(self):
        respDataprev = self.makeRequest("/users/add", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'ma', 'password' : 'admin'} )
        self.assertResponse(respData, count = None, errCode = -1)
        
    def test_loggingIn4(self):
        respDataprev = self.makeRequest("/users/add", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'admin'} )
        self.assertResponse(respData, count = None, errCode = -1)



    def test_loggingIn5(self):
        respDataprev = self.makeRequest("/users/add", method="POST", data = { 'user' : 'mac', 'password' : 'admin'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'mac', 'password' : 'adminn'} )
        self.assertResponse(respData, count = None, errCode = -1)



    def test_loggingIn5(self):
        respDataprev = self.makeRequest("/users/add", method="POST", data = { 'user' : 'this', 'password' : 'that'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'that', 'password' : 'this'} )
        self.assertResponse(respData, count = None, errCode = -1)


class TestResetFixture(testLib.RestTestCase):
    """Test reset Fixture"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)


    def test_ResetFixture1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'get', 'password' : 'employed'} )
        respData1 = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        self.assertResponse(respData1, count = None)
    
    def test_Resetting2(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        respData1 = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        self.assertResponse(respData1, count = None)

    def test_ResetFixture1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'addddd', 'password' : 'usersssss'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'get', 'password' : 'employed'} )
        respData1 = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        self.assertResponse(respData1, count = None)


    def test_ResetFixture1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'addddd', 'password' : 'usersssss'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'get', 'password' : 'employed'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'get', 'password' : 'employed'} )       
        respData1 = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        self.assertResponse(respData1, count = None)
