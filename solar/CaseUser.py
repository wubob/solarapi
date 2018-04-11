#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseUser.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class User_API(unittest.TestCase):
    '''用户 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.username = 'admin'
        self.password = '123456'
        self.app = Public.UserApi(self.base_url)
        
    def test_login(self):                              #+++++++++++++++++++用户登陆
        '''用户登陆'''                          
        response = self.app.User_login(self.username, self.password)
        self.assertIn(response.status_code,[400,403,200])
        print(response.text)
        print(response.status_code)
    
    def test_list(self):                               #+++++++++++++++++++用户列表
        '''用户列表'''
        response = self.app.User_list()
        self.assertEqual(response.status_code,200)
        self.assertIn("admin",response.text)
        print(response.text)
        
   
    def test_get(self):                                #+++++++++++++++++++用户查询
        '''用户查询'''
        response = self.app.User_get()
        self.assertEqual(response.status_code,200)
        print(response.text)
    
    def test_any(self):                                #+++++++++++++++++++用户查看
        '''用户查看'''
        response = self.app.User_any()
        self.assertEqual(response.status_code,200)
        print(response.text)
    
    def test_add(self):                                #+++++++++++++++++++用户增加
        '''用户增加 '''
        response = self.app.User_add()
        self.assertIn(response.status_code,[400,403,201])
        print(response.text)
  
    def test_update(self):                             #+++++++++++++++++++用户修改
        '''用户修改'''
        response = self.app.User_update()
        self.assertIn(response.status_code,[200,204])
        self.assertIn("desc",response.text)
        print(response.text)
  
    def test_password(self):                           #+++++++++++++++++++修改密码
        '''修改密码'''
        response = self.app.User_password()
        self.assertIn(response.status_code,[400,200,403])
        print(response.text)
    
    def test_out(self):
        '''用户登出 '''                                  #+++++++++++++++++++用户登出
        response = self.app.User_out()
        self.assertEqual(response.status_code,204)
        print(response.text)
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(User_API("test_add"))
    testunit.addTest(User_API("test_login"))
    testunit.addTest(User_API("test_list"))
    testunit.addTest(User_API("test_get"))
    testunit.addTest(User_API("test_any"))
    testunit.addTest(User_API("test_update"))
    testunit.addTest(User_API("test_password"))
    testunit.addTest(User_API("test_out"))
    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    