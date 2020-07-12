#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: re_demo.py
# @time: 2020/7/12 11:31 上午

import re

# newdream

str1 = "come on! newdream "
str2 = "china1usa2german3english"

pattern0 = re.compile( r"(\w+),(\w+) (\w+)(?P<sign>.*)" ) #加了原生字符串
pattern1 = re.compile( r"come (\w+)!" )
pattern2 = re.compile( r"\d" )

# result1 = re.match( pattern,str1 )  #匹配以什么开头
# result1 = re.search( pattern1,str1 )  #扫描整个string查找匹配
# result1 = re.split( pattern2,str2 )
# result1 = re.findall( pattern2,str2 ) #搜索string，以列表形式返回全部能匹配的子串
result1 = re.finditer( pattern2,str2 )  #返回的是迭代器
# for r in result1:
#     print(r.group())
# print(result1)




# print( result1.string )
# print( result1.re )
# print( result1.pos )
# print( result1.endpos )
# print( result1.lastindex )
# print( '~~~~~~~~~~~~~~~~~~~~~~~~')
# print( result1.group() )
# print( result1.groups() )
# print( result1.groupdict() )
# print( result1.start() )
# print( result1.end() )
# print( result1.span() )
# print( result1.expand(r"\1") )


str1 = 'summer hot ~~'
pattern3 = re.compile( r"(\w+) (\w+)" )
# str1 = re.sub( pattern3,r"\2 \1",str1 )
# str1 = re.sub( pattern3,r"hello",str1 )
# print( str1 )

# result = re.match( pattern3,str1 )
# print( result.group(1).title() )

def fun(m):
    return m.group(1).title() + ' ' + m.group(2).title()

str1 = re.sub( pattern3,fun,str1 )
print( str1 )

str2 = re.subn( pattern3,r"\2 \1",str1 )
print( str2 )

# 写法二：
str2 = "china1usa2german3english"
v_list = re.split( r"\d" ,str2 )
print( v_list )

