#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: requests_demo01.py
# @time: 2020/7/12 9:30 上午


import requests

response = requests.get('http://www.hnxmxit.com/')
# print( response.json() )  response.encoding
print( response.apparent_encoding )
response.encoding = response.apparent_encoding
print( response.json() )
# print( response.headers )

# print( response.content.decode('utf-8') )