#!/usr/bin/python3
# —*— coding:UTF-8 -*-


from isort import file
from config import *
import json
import requests
import os
requests.packages.urllib3.disable_warnings()


class Threatbook:
    def __init__(self, file):
        self.file = file
        self.api_key = threatbook_key
        self.result = None
        # self.output = output

    def login(self):
        if not self.api_key:
            print('Automatic authorization failed')
            self.api_key = input('ThreatBook API KEY > ').strip()

    def check_file(self):
        file_name = self.file
        url = 'https://api.threatbook.cn/v3/file/upload'
        if os.path.isdir(file_name):
            result=os.listdir(file_name)
            for i in result:
                fields = {
                'apikey': self.api_key,
                'run_time': 60 }
                if os.path.isdir(i):
                    pass
                else:
                    files = {'file' : (i, os.path.join(file_name, i), )}
                    req = requests.post(url=url,data=fields,files=files,verify=False,timeout=5)
                    resp = json.loads(req.text)
                    sha256 = resp['data'].get('sha256')
                    report = 'https://s.threatbook.com/report/file/{0}'.format(sha256)
                    print("文件名字:"+ i + " " + "报告地址："+ report)
        else:
            fields = {'apikey': self.api_key,
                        'run_time': 60 }
            (file_dir,nameaaa) = os.path.split(file_name)
            files =  {'file' : (file_name, open(os.path.join(file_dir, nameaaa), 'rb'))}
            req = requests.post(url=url,data=fields,files=files,verify=False,timeout=5)
            resp = json.loads(req.text)
            sha256 = resp['data'].get('sha256')
            report = 'https://s.threatbook.com/report/file/{0}'.format(sha256)
            print("文件名字:"+ nameaaa + " " + "报告地址："+ report)