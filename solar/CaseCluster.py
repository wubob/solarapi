#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseCluster.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class Cluster_API(unittest.TestCase):
    '''集群 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.ClusterApi(self.base_url)
    
    
    def test_list(self):                               #+++++++++++++++++++集群列表
        '''集群列表'''
        response = self.app.Cluster_list()
        self.assertIn(response.status_code, [200,404,409])
        print(response.text) 
    
    
    def test_get(self):                                #+++++++++++++++++++集群查看
        '''集群查看'''
        response = self.app.Cluster_get()
        self.assertIn(response.status_code, [200,400])
        print(response.text)
    
    
    def test_add(self):                                #+++++++++++++++++++集群添加
        '''集群添加'''
        response = self.app.Cluster_add()
        self.assertIn(response.status_code, [201,400])
        print(response.text) 
    
    def test_update(self):                              #+++++++++++++++++++集群更新
        '''集群更新'''
        response = self.app.Cluster_update()
        self.assertIn(response.status_code, [200,204])
        print(response.text)
    
    def test_delete(self):                              #+++++++++++++++++++集群删除
        '''集群删除'''
        response = self.app.Cluster_delete()
        self.assertIn(response.status_code, [204,423])
        print(response.text)
        
    def test_assign(self):                              #+++++++++++++++++++节点分配
        '''节点分配'''
        response = self.app.Cluster_assign()
        self.assertIn(response.status_code, [200,500])
        print(response.text)
        
    def test_uassign(self):                             #+++++++++++++++++++节点移出
        '''节点移出'''
        response = self.app.Cluster_uassign()
        self.assertIn(response.status_code, [200,404,423])
        print(response.text)
    
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing"+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Cluster_API("test_add"))
    testunit.addTest(Cluster_API("test_list"))
    testunit.addTest(Cluster_API("test_get"))
    testunit.addTest(Cluster_API("test_update"))
    testunit.addTest(Cluster_API("test_assign"))
    testunit.addTest(Cluster_API("test_uassign"))
    testunit.addTest(Cluster_API("test_delete"))

    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    