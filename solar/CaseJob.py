#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseJob.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class Job_API(unittest.TestCase):
    '''异步任务 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.JobApi(self.base_url)
    
    def test_list(self):                                     #+++++++++++++++++++Job列表
        '''Job列表'''
        response = self.app.Job_list()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_get(self):                                      #+++++++++++++++++++Job查看
        '''Job查看'''
        response = self.app.Job_get()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_stop(self):                                     #+++++++++++++++++++Job停止
        '''Job停止'''
        response = self.app.Job_stop()
        self.assertIn(response.status_code, [204,500,404])
        print(response.text)
    
    def test_remove(self):                                   #+++++++++++++++++++Job删除
        '''Job删除'''
        response = self.app.Job_remove()
        self.assertIn(response.status_code, [204,423])
        print(response.text)
    
#     def test_follow(self):                                 #+++++++++++++++++++Job跟踪 xxx
#         '''Job跟踪'''
#         response = self.app.Job_follow()
#         self.assertIn(response.status_code, [200,500,404])
        
    def test_progress(self):                                  #+++++++++++++++++++Job过程
        '''Job过程'''
        response = self.app.Job_progress()
        self.assertIn(response.status_code, [200])
        print(response.text)
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Job_API("test_list"))
    testunit.addTest(Job_API("test_get"))
    testunit.addTest(Job_API("test_progress"))
#     testunit.addTest(Job_API("test_follow"))
    testunit.addTest(Job_API("test_stop"))
    testunit.addTest(Job_API("test_remove"))

    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    