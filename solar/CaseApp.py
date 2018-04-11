#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseApp.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class App_API(unittest.TestCase):
    '''应用 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.APPApi(self.base_url)
      
    def test_2list(self):                                      #+++++++++++++++++++APP列表
        '''APP列表'''
        response = self.app.APP_list()
        self.assertEqual(response.status_code,200)
        print(response.text)

    def test_4get(self):                                       #+++++++++++++++++++APP查看
        '''APP查看'''
        response = self.app.APP_get()
        self.assertEqual(response.status_code,200)
        print(response.text)
        
    
    def test_1add(self):                                        #+++++++++++++++++++APP增加
        '''APP增加'''
        response = self.app.APP_add()
        self.assertIn(response.status_code,[400,201,409])
        print(response.text)
    
        
    def test_3update(self):                                    #+++++++++++++++++++APP更新
        '''APP更新'''
        response = self.app.APP_update()
        self.assertIn(response.status_code,[200,204])
        print(response.text)
            
    
    def test_delete(self):                                    #+++++++++++++++++++APP删除
        '''APP删除'''
        response = self.app.APP_delete()
        self.assertIn(response.status_code,[423,204])
        print(response.text)
        
    def test_5importrevisions(self):                           #+++++++++++++++++++APP版本导入
        '''APP版本导入'''
        response = self.app.APP_importrevisions()
        self.assertEqual(response.status_code,201)
        print(response.text)
        
    def test_6revisions(self):                                 #+++++++++++++++++++APP版本列表
        '''APP版本列表'''
        response = self.app.APP_revisionslist()
        self.assertEqual(response.status_code,200)
        print(response.text)
    
    def test_7getrevisions(self):                               #+++++++++++++++++++APP版本查看
        '''APP版本查看'''
        response = self.app.APP_getrevisions()
        self.assertEqual(response.status_code,200)
        print(response.text)
    
    
    def test_8exportrevisions(self):                           #+++++++++++++++++++APP版本导出
        '''APP版本导出'''
        response = self.app.APP_exportrevisions()
        self.assertEqual(response.status_code,200)
        print(response)
        print(response.text)

    def test_9deploy(self):                                    #+++++++++++++++++++APP版本部署
        '''APP版本部署'''
        response = self.app.APP_deploy()
        self.assertIn(response.status_code,[201,400])
        print(response.text)
        
        
    def tearDown(self):
        pass
#         response = self.app.APP_add()
#         self.assertIn(response.status_code,[400,201,409])
#         print(response.text)
#         time.sleep(seconds)
#         response = self.app.APP_staus()
#         print(response.text)
       
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(App_API("test_1add"))
    testunit.addTest(App_API("test_2list"))
    testunit.addTest(App_API("test_3update"))
    testunit.addTest(App_API("test_4get"))
    testunit.addTest(App_API("test_5importrevisions"))
    testunit.addTest(App_API("test_6revisions"))
    testunit.addTest(App_API("test_7getrevisions"))
    testunit.addTest(App_API("test_8exportrevisions"))
    testunit.addTest(App_API("test_9deploy"))
    testunit.addTest(App_API("test_delete"))
    
    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    