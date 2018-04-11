#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import random

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin
    
class UserApi(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        self.cookie=""
        self.User_login("admin", "123456")
        
    def User_login(self, username, password):
        url = urljoin(self.base_url, '/api/users/login')
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, json.dumps(data),headers=self.headers)
        self.cookie=response.cookies
        return response
 
    def User_list(self):
        url = urljoin(self.base_url, '/api/users')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def User_get(self):
        url = urljoin(self.base_url, '/api/users/'+json.loads(self.User_list().text)[0]["id"])
        response = requests.get(url,cookies=self.cookie, headers=self.headers)
        return response
    
    def User_any(self):
        url = urljoin(self.base_url, '/api/users/any')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
  
    def User_add(self):
        url = urljoin(self.base_url, '/api/users')
        data = {
            "name": "admin",
            "password": "123456",
            "desc": "the only privileged user",
         }
        response = requests.post(url, json.dumps(data),headers=self.headers)
        return response
  
    def User_update(self):
        url = urljoin(self.base_url, '/api/users/'+json.loads(self.User_list().text)[0]["id"])
        data = {"desc":"new1  new2 new3 description text"}
        response = requests.patch(url,json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
  
    def User_password(self):
        url = urljoin(self.base_url, '/api/users/'+json.loads(self.User_list().text)[0]["id"]+r'/'+'change_password')
        data = {"old": "123456","new": "123456"}
        response = requests.patch(url,json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def User_out(self):
        url = urljoin(self.base_url, '/api/users/logout')
        response = requests.delete(url,cookies=self.cookie,headers=self.headers)
        return response
  
class NodeApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
        
    
    def Node_list(self):
        url = urljoin(self.base_url, '/api/nodes')
        response = requests.get(url,cookies=self.cookie, headers=self.headers)
        return response
    
    def Node_get(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"])
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_add(self):
        url = urljoin(self.base_url, '/api/nodes?exec_id=1111122222')
        data = {"addr": "192.168.1.241:22","user": "root","password": "123","privkey": "","timeout": 10}
        response = requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_set(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'attrs')
        data= {
              "manage_ip": "192.168.1.244",
              "internal_ip": "10.0.0.5",
              "env": {
                "os": "centos7",
                "zone": "bj"
              },
              "custom": {
                "admin": "xbwu@dataman-inc.com",
                "ssd": "true"
              },
              "host_name": "wxbss244"
            }
        response = requests.put(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_batchSet(self):
        url = urljoin(self.base_url, '/api/nodes/attrs')
        csvfile ='D:\\Project\\456.csv'
        with open(csvfile,'r') as f:
            data = f.read()
        response = requests.put(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
#     def Node_watch(self):
#         url = urljoin(self.base_url, 'api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'events')
#         response = requests.get(url, cookies=self.cookie,headers=self.headers)
#         return response
    
    def Node_exec(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'exec')
        data = {"command": "for((i=1;i<=1;i++));do sleep 1;echo $i;done"}
        response = requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_delete(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"])
        response = requests.delete(url,cookies=self.cookie,headers=self.headers)
        return response
    
    
    def Node_upgrade(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'upgrade')
        response = requests.put(url,cookies=self.cookie,headers=self.headers)
        return response
    
    
    def Node_alabel(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'labels')
        data ={"name": "wxb123", "sex": "Man22123"}
        response = requests.put(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response

    def Node_ulabel(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'labels')
        data ={"name": "wxb123", "sex": "Man22123"}
        response = requests.delete(url, data=json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_lyum(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'repos')
        response = requests.get(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_ayum(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'repos?name=demorepo')
        data = [
            {
                    "title": "docker",
                    "name": "docker stable repo",
                    "baseurl": "https://download.docker.com/centos/7/stable",
                    "gpgcheck":False,
            },
                {
                    "title": "update",
                    "name": "docker update repo",
                    "baseurl": "https://download.docker.com/centos/7/update",
                    "gpgcheck":True,
                    "gpgkey": "http://download.docker.com/centos/7/update/RPM-GPG-KEY-7-DOCKER"
                }
             ]
        response = requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_dlabel(self):
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'repos?name=demorepo')
        response = requests.delete(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Node_docker(self):
        # watch node docker events stream  GET /api/nodes/df5812ce5f1eaf5f/docker/events HTTP/1.1
        # restart node docker container    POST /api/nodes/df5812ce5f1eaf5f/docker/containers/mysql-container/restart HTTP/1.1
        url = urljoin(self.base_url, '/api/nodes/'+json.loads(self.Node_list().text)[0]["id"]+'/'+'docker/info')
        response = requests.get(url,cookies=self.cookie,headers=self.headers)
        return response
    
class ClusterApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def Node_list(self):
        url = urljoin(self.base_url, '/api/nodes')
        response = requests.get(url,cookies=self.cookie, headers=self.headers)
        return response
    
    def Cluster_list(self):
        url = urljoin(self.base_url, '/api/clusters')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Cluster_get(self):
        url = urljoin(self.base_url, '/api/clusters/'+json.loads(self.Cluster_list().text)[0]["id"])
        response = requests.get(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Cluster_add(self): 
        url = urljoin(self.base_url, '/api/clusters')
        data = {
            "name": "demo"+str(random.randint(1,100)),
            "desc": "demo123 cluster",
            "attrs": {
                "admin": "admin@demo.net",
                "zone": "bj"
                    }
                } 
        response = requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
        
    
    def Cluster_update(self): 
        url = urljoin(self.base_url, '/api/clusters/'+json.loads(self.Cluster_list().text)[0]["id"])
        data = {
            "desc": "demo2 cluster",
            "attrs": {
                "admin": "admin2@demo.net",
                "zone": "bj111111111111"
                    }
            }
        response = requests.patch(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Cluster_delete(self): 
        url = urljoin(self.base_url, '/api/clusters/'+json.loads(self.Cluster_list().text)[0]["id"])
        response = requests.delete(url,cookies=self.cookie,headers=self.headers)
        return response
          
    
    def Cluster_assign(self): 
        url = urljoin(self.base_url, '/api/clusters/'+json.loads(self.Cluster_list().text)[0]["id"]+r'/'+json.loads(self.Node_list().text)[0]["id"])
        response = requests.put(url,cookies=self.cookie,headers=self.headers)
        return response
    
    
    def Cluster_uassign(self): 
        url = urljoin(self.base_url, '/api/clusters/'+json.loads(self.Cluster_list().text)[0]["id"]+r'/'+json.loads(self.Node_list().text)[0]["id"])
        response = requests.delete(url,cookies=self.cookie,headers=self.headers)
        return response
    
class JobApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def Job_list(self):
        url = urljoin(self.base_url, '/api/jobs')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Job_get(self):
        url = urljoin(self.base_url, '/api/jobs/'+json.loads(self.Job_list().text)[0]["id"])
        response = requests.get(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Job_stop(self):
        url = urljoin(self.base_url, '/api/jobs/'+json.loads(self.Job_list().text)[0]["id"]+r'/'+'stop')
        response = requests.patch(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Job_remove(self):
        url = urljoin(self.base_url, '/api/jobs/'+json.loads(self.Job_list().text)[0]["id"])
        response = requests.delete(url, cookies=self.cookie,headers=self.headers)
        return response
    
#     def Job_follow(self):
#         url = urljoin(self.base_url, '/api/jobs/'+json.loads(self.Job_list().text)[0]["id"]+r'/'+'follow')
#         response = requests.get(url, cookies=self.cookie,headers=self.headers)
#         return response
     
    def Job_progress(self):
        url = urljoin(self.base_url, '/api/jobs/'+json.loads(self.Job_list().text)[0]["id"]+r'/'+'progress')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response

class APPApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def APP_list(self):
        url = urljoin(self.base_url, '/api/apps')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_get(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_add(self):
        url = urljoin(self.base_url, '/api/apps')
        data = {"name": "nginxwxb",
                "desc": "nginx app",
                "version":"1.13.7",
                "release":"nginx"}
        response=requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_update(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb')
        data = {"desc": "nginx update app"}
        response=requests.patch(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_delete(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb')
        response = requests.delete(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_importrevisions(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb/revisions')
        # urlAPPImportRevision='http://192.168.1.241:88/api/apps/nginxwxb/revisions?tar=http://192.168.1.104:8089/Desktop/tar/nginx.tar' # url方式
        tar="D:\\Project\\app\\nginx.tar"
        data = open(tar, 'r').read()
        # rAPPImportRevision = requests.post(urlAPPImportRevision,cookies=rlogin.cookies,headers=headers) # url方式
        response = requests.post(url, data=data,cookies=self.cookie,headers=self.headers)
        
        return response
    
    def APP_revisionslist(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb/revisions')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_getrevisions(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb/revisions/'+json.loads(self.APP_revisionslist().text)[0]["id"])
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_exportrevisions(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb/revisions/'+json.loads(self.APP_revisionslist().text)[0]["id"]+r'/'+'export')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def APP_deploy(self):
        
        url = urljoin(self.base_url, '/api/apps/nginxwxb/revisions/'+json.loads(self.APP_revisionslist().text)[0]["id"]+r'/'+'deploy')
        data ={
            
            "name": "DataMan"+str(random.randint(1,100)),
            "desc": "nginx20171225  nginx app instance",
            "binded_datas": {
                "PORT": "81"
                },
            "binded_labels": {
            
                },
            "binded_cluster": "demo123",
            "replicas": 1
            }
        response = requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Job_list(self):
        url = urljoin(self.base_url, '/api/jobs')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Job_get(self):
        url = urljoin(self.base_url, '/api/jobs/'+json.loads(self.Job_list().text)[0]["id"])
        response = requests.get(url,cookies=self.cookie,headers=self.headers)
        return response
    
#     def APP_staus(self):
#         


class InstanceApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
        
    def APP_revisionslist(self):
        url = urljoin(self.base_url, '/api/apps/nginxwxb/revisions')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_list(self):
        url = urljoin(self.base_url, '/api/instances')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
        
    
    def Instance_get(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"])
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_update(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"])
        data ={"desc": "修改实例节点123"}
        response = requests.patch(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_start(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'start')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
     
    def Instance_reload(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'reload')
        data ={"PORT": "88"}
        response = requests.patch(url,json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response

    def Instance_log(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'?script=install') 
        # detect|install|uninstall|reinstall|start|stop|reload|upgrade
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_stop(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'stop')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_restart(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'restart')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_apply(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'apply?revision_id='+json.loads(self.APP_revisionslist().text)[0]["id"])
        data ={"PORT": "88","USER": "admin"}
        response = requests.patch(url,json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
#     def Instance_events(self):
#         url = urljoin(self.base_url, '/api/instances/events?instance_id='+json.loads(self.Instance_list().text)[0]["id"]) 
#         response = requests.get(url, cookies=self.cookie,headers=self.headers)
#         return response
    
    def Instance_remove(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'?force=true')
        response = requests.delete(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Instance_scalelogs(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'scalelogs') 
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response

class TaskApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def Instance_list(self):
        url = urljoin(self.base_url, '/api/instances')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
        
    def Task_list(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Task_get(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"])
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Task_start(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"]+r'/'+'start')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Task_stop(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"]+r'/'+'stop')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Task_restart(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"]+r'/'+'restart')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response

    def Task_log(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"]+r'/'+'log?script=start') 
        # detect|install|uninstall|reinstall|start|stop|restart|reload|upgrade|statecheck|enable|disable
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Task_enable(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"]+r'/'+'enable')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
    
    def Task_disable(self):
        url = urljoin(self.base_url, '/api/instances/'+json.loads(self.Instance_list().text)[0]["id"]+r'/'+'tasks'+r'/'+json.loads(self.Task_list().text)[0]["id"]+r'/'+'disable')
        response = requests.patch(url,cookies=self.cookie,headers=self.headers)
        return response
    
      
class SshkeyApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def Sshkey_list(self):
        url = urljoin(self.base_url, '/api/sshkeys')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Sshkey_get(self):
        url = urljoin(self.base_url, '/api/sshkeys/'+json.loads(self.Sshkey_list().text)[0]["id"])
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
     
    def Sshkey_add(self):
        url = urljoin(self.base_url, '/api/sshkeys')
        data={
            "name": "DataMan3",
            "desc": "DataMan3 ssh key",
            "privkey": '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA05QZhTulLkl/DChRMNsnqetjhdUhYVhaOEvq0GFBhpxuwVox
C6kv4UnpfQ7mjhBTm8OJXXNFdViK6URigzh97KMm+JKVGEdhGVIa3oIU6S0OSpVP
0n7GjlyG512kJ2o7x8im70GblLv4S/+/A7COitfigktVRR4CAWYaPoNExHavbCVZ
cvKlCcf3d+BFC4n026aoisvhT0s2cQiMDgh3VpiQtinLLCFc7PDukVmGIH/wabDt
JO3IzzWNqmIliLZuvSCYtlEdfyTlzXKA5EG0Xz9wWqItYUSkBykWPNtbXZeir2Pk
SkbAnPiiu/qJx+873pOs/J53nmzd18zqsRx+wQIDAQABAoIBAQCHkCHV6wSIJtE/
cemrmw/L4KVQz+FmZNzRq1rVjysT29FfE7HPHeUuvVPcLBrvNWjMqbmu5bfAWy4O
DiHsn9qXL2Y96HWdK8b8GU5b+Q765EJ+6TJO1anU91X8klQmaPvKozbKn8fWwaVy
1HeIHq0GKxLXlvsYoQR57viryyHZmmO4nXkM2Ah8GOPRC7CGiSJJdIKsNxt4MDxU
xTG+gupIJVDVdWIpx35vjea/ydQRzwcsTSmC1qAk9dxnhrm67EZw6DwgTkXCYyc1
loJcxBGUNNtLVuaXZh1VFNUO8BBfwzPLA1OCjXJokKrzzMGWXGdWyUiQF74eCuR+
wH+NW+XNAoGBAO2XmS7ieJgi8FVmwUEpFZlxhrLYqTMCKpXU8hL+prLS1RJ5rY0h
knlyCPjJ5SYOApC1bq9l5PbbRyv7RJChxUJS0O6gwfTE5U/86gAFQ6+OFbz470Y9
I8zg2o5laO9RmYytoUO1WtbO0Fba6dXkoEol4oBAQuXgby22Hcivs/BLAoGBAOP4
i+NLODGKidE66n1uFfQDePNCRwSoMw3Xaoj2L9zSPaZSipJQErNfOck6OxACLk7Q
kB6eBVVAJOBZfrEjKels4srG1QTdFzXTeTUdHQky40nl5SaqUKUjc9viRIBAeWKb
0CiNvwTCD7fT7EFTuP1F84ojfbb7LQMgQe+Oth2jAoGAMBnE9Wz8JTDNnzySW3LJ
4KrPLl4WwzDpFjRqXdYYQZPVd0wTCsOFN/kSP+v/7FhhxJI2umPSmveBzTGti+p0
WR0TF3yMR9Wk5zC43xAxx9ToKb3sEzhFizDqjnGRcQIAKC7uuxp4LYzpOOxQ8vC6
Usigtn5MDOYHHCYGmZ6Yu0kCgYEA4IGcWfpw27EgqnIIDgCFFCr7SS2DPR3cMYxs
uXchialu10ZAe3jqAcYM5ZQ4KDrNmgahd9WNUPh7mInqT85ebygxbRtFG6YUPokF
u/3w42c/GT6TXnGqPAdfCTOa3GciY68o31dAwBHRYusMpwUpkBv8jJUJMFPKb2Ks
LJxx01sCgYEAi/moP9NQaupSgTm1rFZf0wuxsT4Tq0KgW5wiyfPNWvVESjGRRJyf
LA8ueg4+/MH0ChmzgqDuAN0c5eNTad235J9B00OzndkoestiodQBG1yx0tR/nS1M
O9DET+UQwwCXCHkm91xmY8GFJg6kMrvsHbY73NfHd9Ie3BsfpggDbDk=
-----END RSA PRIVATE KEY-----
''',
            }
        response = requests.post(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Sshkey_update(self):
        url = urljoin(self.base_url, '/api/sshkeys/'+json.loads(self.Sshkey_list().text)[0]["id"])
        data = { "desc": "new new new DataMan3 ssh key" }
        response=requests.patch(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Sshkey_remove(self):
        url = urljoin(self.base_url, '/api/sshkeys/'+json.loads(self.Sshkey_list().text)[0]["id"])
        response = requests.delete(url, cookies=self.cookie,headers=self.headers)
        return response
    
class SettingApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def Setting_get(self):
        url = urljoin(self.base_url, '/api/settings')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Setting_update(self):
        url = urljoin(self.base_url, '/api/settings')
        data ={
          "advertise_addr": "192.168.1.241:88,192.168.1.242:88,192.168.1.243:88,192.168.1.244:88",
          "log_level": "debug",
          "enable_auth": True,
        }
        response=requests.patch(url, json.dumps(data),cookies=self.cookie,headers=self.headers)
        return response
    
    def Setting_reset(self):
        url = urljoin(self.base_url, '/api/settings/reset')
        response=requests.put(url, cookies=self.cookie,headers=self.headers)
        return response
    
    
class OtherApi(UserApi):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers={'Content-Type':'application/json'}
        super().__init__(base_url)
    
    def Other_version(self):
        url = urljoin(self.base_url, '/api/version')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Other_info(self):
        url = urljoin(self.base_url, '/api/info')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Other_dump(self):
        url = urljoin(self.base_url, '/api/debug/dump?name=general')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    def Other_ping(self):
        url = urljoin(self.base_url, '/api/ping')
        response = requests.get(url, cookies=self.cookie,headers=self.headers)
        return response
    
    
       
# if __name__ == '__main__':
#     base_url = "http://192.168.1.241"
#     obj = NodeApi(base_url)
#     print(obj.Node_list())
#     
#     print(obj.User_login('admin', '123456'))