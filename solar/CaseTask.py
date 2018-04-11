#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseTask.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class Task_API(unittest.TestCase):
    '''任务  API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.TaskApi(self.base_url)

    def test_list(self):                                       #+++++++++++++++++++任务列表
        '''任务列表'''
        response = self.app.Task_list()
        self.assertIn(response.status_code, [200])
        print(response.text)   
    
    def test_get(self):                                        #+++++++++++++++++++任务查看
        '''任务查看'''
        response = self.app.Task_get()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_start(self):                                      #+++++++++++++++++++任务启动
        '''任务启动'''
        response = self.app.Task_start()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_stop(self):                                       #+++++++++++++++++++任务停止
        '''任务停止'''
        response = self.app.Task_stop()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_restart(self):                                    #+++++++++++++++++++任务重启
        '''任务重启'''
        response = self.app.Task_restart()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_log(self):                                         #+++++++++++++++++++任务日志
        '''任务日志'''
        response = self.app.Task_log()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def Task_enable(self):                                       #+++++++++++++++++++任务激活
        '''任务激活'''
        response = self.app.Task_enable()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def Task_disable(self):                                      #+++++++++++++++++++任务关闭
        '''任务关闭'''
        response = self.app.Task_disable()
        self.assertIn(response.status_code, [200])
        print(response.text)
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Task_API("test_start"))
    testunit.addTest(Task_API("test_list"))
    testunit.addTest(Task_API("test_get"))
    testunit.addTest(Task_API("test_stop"))
    testunit.addTest(Task_API("test_restart"))
    testunit.addTest(Task_API("test_log"))
    testunit.addTest(Task_API("Task_disable"))
    testunit.addTest(Task_API("Task_enable"))
    
      
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    