#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseOther.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class Other_API(unittest.TestCase):
    '''其他  API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.OtherApi(self.base_url)
            
    def test_version(self):                                        #+++++++++++++++++++版本查询
        '''版本查询'''
        response = self.app.Other_version()
        self.assertEqual(response.status_code,200)
        self.assertIn("version",response.text)
        self.assertIn("go_version",response.text)
        print(response.text)
                
    def test_ping(self):                                           #+++++++++++++++++++ping查看
        '''ping查看'''
        response = self.app.Other_ping()
        self.assertEqual(response.status_code,200)
        self.assertIn("OK",response.text)
        print(response.text)
        
    def test_info(self):                                           #+++++++++++++++++++信息查询
        '''信息查询'''
        response = self.app.Other_info()
        self.assertEqual(response.status_code,200)
        self.assertIn("version",response.text)
        print(response.text)
               
    def test_dump(self):                                           #+++++++++++++++++++查看调试
        '''查看调试'''
        response = self.app.Other_dump()
        self.assertEqual(response.status_code,200)
        print(response.text)
               
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Other_API("test_version"))
    testunit.addTest(Other_API("test_ping"))
    testunit.addTest(Other_API("test_info"))
    testunit.addTest(Other_API("test_dump"))
       
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    