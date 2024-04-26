# -*- coding: utf-8 -*-
# 获取时间函数
import datetime


def get_now_time():
    current_time = datetime.datetime.now()
    now_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return now_time