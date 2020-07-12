#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: eval_demo.py
# @time: 2020/7/12 9:11 上午

import ast

sum = eval("66+32")
print( sum )

print( ast.literal_eval("{'name':'linux','age':18}") )

print(eval("{'name':num,'age':'33'}",{"num":18}))

age = 10
print(eval("{'name':'linux','age':age}",{"age":18},locals()))

ast.literal_eval( "__import__('os').system('ls')" )
