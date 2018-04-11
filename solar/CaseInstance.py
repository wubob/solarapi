#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseInstance.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public
import json

class Instance_API(unittest.TestCase):
    '''实例 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.InstanceApi(self.base_url)

    def test_2list(self):                                       #+++++++++++++++++++Instance列表
        '''Instance列表'''
        response = self.app.Instance_list()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_3get(self):                                        #+++++++++++++++++++Instance查看
        '''Instance查看'''
        response = self.app.Instance_get()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_4update(self):                                     #+++++++++++++++++++Instance更新
        '''Instance更新'''
        response = self.app.Instance_update()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_1start(self):                                      #+++++++++++++++++++Instance启动
        '''Instance启动'''
        response = self.app.Instance_start()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_5stop(self):                                       #+++++++++++++++++++Instancen停止
        '''Instancen停止'''
        response = self.app.Instance_stop()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_6restart(self):                                    #+++++++++++++++++++Instancen重启
        '''Instancen重启'''
        response = self.app.Instance_restart()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_8apply(self):                                      #+++++++++++++++++++Instancen升降级
        '''Instancen升降级'''
        response = self.app.Instance_apply()
        self.assertIn(response.status_code, [200,403])
        print(response.text)
      
    def test_7reload(self):                                      #+++++++++++++++++++Instance重载
        '''Instance重载'''
        response = self.app.Instance_reload()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_cremove(self):                                      #+++++++++++++++++++Instance删除
        '''Instance删除'''
        response = self.app.Instance_remove()
        self.assertIn(response.status_code, [204,403])
        print(response.text)
    
    def test_9log(self):                                         #+++++++++++++++++++Instance日志
        '''Instance日志'''
        response = self.app.Instance_log()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
#     def test_aevents(self):                                       #+++++++++++++++++++Instancen监听
#         '''Instancen监听'''
#         response = self.app.Instance_events()
#         self.assertIn(response.status_code, [200])
#         print(response.text)
    
    def test_bscalelogs(self):                                    #+++++++++++++++++++扩缩历史
        '''扩缩历史'''
        response = self.app.Instance_scalelogs()
        self.assertIn(response.status_code, [200])
        print(response.text)
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Instance_API("test_1start"))
    testunit.addTest(Instance_API("test_2list"))
    testunit.addTest(Instance_API("test_3get"))
    testunit.addTest(Instance_API("test_4update"))
    testunit.addTest(Instance_API("test_5stop"))
    testunit.addTest(Instance_API("test_6restart"))
    testunit.addTest(Instance_API("test_7reload"))
    testunit.addTest(Instance_API("test_8apply"))
    testunit.addTest(Instance_API("test_9log"))
#     testunit.addTest(Instance_API("test_aevents"))
    testunit.addTest(Instance_API("test_bscalelogs"))
    testunit.addTest(Instance_API("test_cremove"))
    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    