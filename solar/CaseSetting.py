#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseSetting.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class Setting_API(unittest.TestCase):
    '''全局设置 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.SettingApi(self.base_url)
    
    def test_list(self):                                     #+++++++++++++++++++全局查询
        '''全局查询'''
        response = self.app.Setting_get() 
        self.assertEqual(response.status_code,200)
        self.assertIn("advertise_addr",response.text)
        print(response.text)
    
    def test_update(self):                                   #+++++++++++++++++++全局修改
        '''全局修改'''
        response = self.app.Setting_update()
        self.assertEqual(response.status_code,200)
        self.assertIn("advertise_addr",response.text)
        print(response.text)
         
    def test_reset(self):                                    #+++++++++++++++++++全局重置
        '''全局重置'''
        response = self.app.Setting_reset()
        self.assertEqual(response.status_code,200)
        self.assertIn("advertise_addr",response.text)
        print(response.text)
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Setting_API("test_reset"))
    testunit.addTest(Setting_API("test_update"))
    testunit.addTest(Setting_API("test_list"))
 
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    