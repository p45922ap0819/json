# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:54:01 2019

@author: user
"""

import csv

allscore = []


def score_input():
    name = int(input("請輸入學生姓名: "))
    chinese = int(input("請輸入中文成績: "))
    english = int(input("請輸入英文成績: "))
    math = int(input("請輸入數學成績: "))
    average = (chinese+english+math)/3
    
    allscore.append(name,chinese,english,math,average)
    
while(True)



