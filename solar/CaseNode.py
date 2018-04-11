#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseNode.py

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
import unittest, time
import HTMLTestRunner
import Public

class Node_API(unittest.TestCase):
    '''节点API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88' 
        self.app = Public.NodeApi(self.base_url)   

    def test_2list(self):                               #+++++++++++++++++++节点列表
        '''节点列表'''
        response = self.app.Node_list()
        self.assertEqual(response.status_code,200)
        print(response.text)
        
    def test_3get(self):                                #+++++++++++++++++++节点查询
        '''节点查询'''
        response = self.app.Node_get()
        self.assertIn(response.status_code, [200,400])
        print(response.text)
    
    def test_1add(self):                                #+++++++++++++++++++节点增加
        '''节点增加'''
        response = self.app.Node_add()
        self.assertIn(response.status_code,[400,500,200,409])
        print(response.text)
    
    def test_4set(self):                                #+++++++++++++++++++节点设置
        '''节点设置'''
        response = self.app.Node_set()
        self.assertEqual(response.status_code,200)
        print(response.text)
        
    def test_5batchset(self):                           #+++++++++++++++++++批量设置 
        '''批量设置'''
        response = self.app.Node_batchSet()
        self.assertIn(response.status_code,[409,200])
        print(response.text)
        
        
#     def test_6watch(self):                               #+++++++++++++++++++监听事件 xxx
#         '''监听事件'''
#         response = self.app.Node_watch()  
#         self.assertEqual(response.status_code,200)
    
    def test_7exec(self):                                  #+++++++++++++++++++远程命令
        '''远程命令'''
        response = self.app.Node_exec()  
        self.assertEqual(response.status_code,200)
        print(response.text)
    
    def test_fdelete(self):                              #+++++++++++++++++++节点删除
        '''节点删除'''
        response = self.app.Node_delete()  
        self.assertIn(response.status_code, [204,500,423])
        print(response.text)
        
    
    def test_8upgrade(self):                             #+++++++++++++++++++节点升级
        '''节点升级'''
        response = self.app.Node_upgrade()
        self.assertIn(response.status_code, [200,500,403])
        print(response.text)
     
    def test_9alabel(self):                              #+++++++++++++++++++设置标签
        '''设置标签'''
        response = self.app.Node_alabel()
        self.assertIn(response.status_code, [200,400])
        print(response.text)
           
    def test_aulabel(self):                              #+++++++++++++++++++删除标签
        '''删除标签'''
        response = self.app.Node_ulabel()
        self.assertIn(response.status_code, [200,400])
        print(response.text)
           
    def test_clyum(self):                                #+++++++++++++++++++列出YUM
        '''列出YUM'''
        response = self.app.Node_lyum()
        self.assertIn(response.status_code, [200])
        print(response.text)
        
    def test_bayum(self):                                #+++++++++++++++++++增加YUM
        '''增加YUM'''
        response = self.app.Node_ayum()
        self.assertIn(response.status_code, [200])
        print(response.text)
    
    def test_ddyum(self):                                #+++++++++++++++++++删除YUM
        '''删除YUM'''
        response = self.app.Node_dlabel()
        self.assertIn(response.status_code, [204])  
        print(response.text)
    
    def test_edocker(self):                              #+++++++++++++++++++Docker API
        '''Docker API'''
        response = self.app.Node_docker()
        self.assertIn(response.status_code, [204,200])  
        print(response.text)
    
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    
    testunit=unittest.TestSuite()
    testunit.addTest(Node_API("test_1add"))
    testunit.addTest(Node_API("test_2list"))
    testunit.addTest(Node_API("test_3get"))
    testunit.addTest(Node_API("test_4set"))
    testunit.addTest(Node_API("test_5batchset"))
#   testunit.addTest(Node_API("test_6watch"))
    testunit.addTest(Node_API("test_7exec"))
    testunit.addTest(Node_API("test_8upgrade"))
    testunit.addTest(Node_API("test_9alabel"))
    testunit.addTest(Node_API("test_aulabel"))
    testunit.addTest(Node_API("test_bayum"))
    testunit.addTest(Node_API("test_clyum"))
    testunit.addTest(Node_API("test_ddyum"))
    testunit.addTest(Node_API("test_edocker"))
    testunit.addTest(Node_API("test_fdelete"))
    
    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    