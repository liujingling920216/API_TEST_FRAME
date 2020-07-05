#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: read_excel.py
# @time: 2020/7/1 9:13 下午

import os
import xlrd

excel_path = os.path.join( os.path.dirname(__file__) , 'data/test_data.xlsx' )
# print( excel_path )

wb = xlrd.open_workbook( excel_path )  # 创建工作薄对象
sheet = wb.sheet_by_name("Sheet1")  #创建表格对象
sheet = wb.sheet_by_index(0)#
# cell_value = sheet.cell_value( 3,2 )  # 直接取值  行列下标从0开始 row  col
cell_value = sheet.cell_value( 0,0 )
# print( cell_value )
cell_value = sheet.cell_value( 1,0 )
# print( cell_value )
cell_value = sheet.cell_value( 2,0 )  # 对于合并的左上角首个单元格会返回真实值
# print( cell_value )
# 2,0  3,0  4,0  学习python编程


# 处理方式：xlrd
merged = sheet.merged_cells  # 返回一个列表  起始行，结束行，起始列，结束列）

# 逻辑： 凡是在merged_cells属性范围内的单元格 它的值都要等于左上角首个单元格的值
row_index = 3 ; col_index = 0

for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
    if (row_index >= rlow and row_index < rhigh):  # 行坐标判断  1<=3<5
        if (col_index >= clow and col_index < chigh):  # 列坐标判断 0<=0<1
            # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
            cell_value = sheet.cell_value(rlow,clow)
# print( cell_value )


def get_merged_cell_value01(row_index,col_index):
    """只能完成合并单元格数据的获取"""
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
    return cell_value

print( get_merged_cell_value01(3,0) )

def get_merged_cell_value02(row_index,col_index):
    """既能获取普通单元格的数据又能获取合并单元格数据"""
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                break; # 防止循环去进行判断出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

print( get_merged_cell_value02(4,0) )

for i in range(1,9):
    print(get_merged_cell_value02(i, 0))
# print( sheet.merged_cells )
