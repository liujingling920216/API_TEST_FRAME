#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: jsonpath_demo.py
# @time: 2020/7/12 10:59 上午

import jsonpath

d1 = {"access_token":"35_E4Y_WlCgAo0IqX58BZTPttdPXxYrT_8VaSTCuptkRR3NwTK_SSs_KPAifD_mOXk4ob56_v6cdPipasgj-K6cA8MpFcHFBBH7ofSu1Mtt2czWs84OScxOXuVQt99WuWn2i68cN3zujvuJhzTWGMEiAAAZFX","expires_in":7200}
print( d1['access_token'] )
print( jsonpath.jsonpath(d1,'$.access_token')[0] )  # 'aaahello' ==>'aaa(.+?)lo' 目的一致 取数据

# print(  )
#
d2 = {   "tags":[{ "id":1, "name":"每天一罐可乐星人", "count":0 },
                    {   "id":2,   "name":"星标组",   "count":0 },
        {  "id":127,  "name":"广东",  "count":5 }   ]
      }
#  放入bejson
print( d2['tags'][1]['name'] )
print( jsonpath.jsonpath(d2,'$.tags[1].name')[0] )