#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url='http://www.bluecore.com.cn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

response = requests.get(url=url,headers=headers).text

print(response)