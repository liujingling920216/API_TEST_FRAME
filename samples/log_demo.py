#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: log_demo.py
# @time: 2020/7/5 2:15 下午

import logging

logger = logging.getLogger("logger")
logger.setLevel(10) # 10,20,30,40,50
handler1 = logging.StreamHandler()  #控制台
handler1.setLevel(30)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)

handler2 = logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(10)
handler2.setFormatter(formatter)
logger.addHandler( handler2 )

logger.info( "hello" )

