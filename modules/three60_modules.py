#!/usr/bin/python3
# —*— coding:UTF-8 -*-


from tabnanny import filename_only
from isort import file
from config import *
import json
import requests
import os
requests.packages.urllib3.disable_warnings()


class Three_360:
    def __init__(self, file):
        self.file = file
        self.api_key = key_360
        self.result = None
        # self.output = output

    def login(self):
        if not self.api_key:
            print('Automatic authorization failed')
            self.api_key = input('360 API KEY > ').strip()
    def check_file(self):
        file_name = self.file
        url = "https://ata.360.cn/api/v1/task/submit"
        headers = {'Authorization': 'JWT ' + self.api_key}
        pass