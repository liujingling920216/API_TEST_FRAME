#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: replace_demo.py
# @time: 2020/7/12 3:08 下午

import re
import ast
import requests


temp_variables = {"token":"hello"}

params = '{"access_token":${token}}'   # 建议考试1个以上的情况
value = re.findall('\\${\w+}',params)[0]
print(value)
params = params.replace( value,'"%s"'%temp_variables.get(value[2:-1]) ) # '"'+%temp_variables.get(value[2:-1])+'"'
print( params )

temp_variables = {"token":"123456","number":"123","age":"66"}
str1 = '{"access_token":${token},${age}==>${number}}'
for v in re.findall('\\${\w+}',str1):
    str1 = str1.replace( v,temp_variables.get( v[2:-1] ) )
print( str1 )


# str1 = re.sub('\\${\w+}',r'123456',str1,1)
# str1 = re.sub('\\${\w+}',r'123456',str1,1)
# print( str1 )

# dicta = {"token":"123","age":18}
# print( dicta["token"] )
# print( dicta.get( "token" ) )



# requests.get(url = "/cgi-bin/tags/delete",
#              params = ast.literal_eval( params )
#              )

temp_variables = {}
#第一个用例 添加标签
temp_variables["token"] = "35_an_RI1hEsxPGpt"

# temp_variables = {}
#第二个用例，删除标签 获取token ==
temp_variables["token"] = "36666gfgfgf"

print( temp_variables )

