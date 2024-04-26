# -*- coding: utf-8 -*-
import yaml
from selenium.webdriver.common.by import By

with open('./element/element_dan.yaml', 'r', encoding='utf-8') as file:
    element_data_yaml = yaml.safe_load(file)

# 创建字典用于存储定位方式和元素名称的映射关系
LOCATE_MODE = {}

# 定位方式和元素值的映射关系
mapping = {
    'id': By.ID,
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'class': By.CLASS_NAME,
    'text': By.LINK_TEXT
}

# 提取定位方式和元素值
for element_name, element_data in element_data_yaml.items():
    by_method = mapping.get(element_data['By'].lower())  # 获取对应的 By 对象字符串
    element_value = element_data['element']  # 获取元素值
    LOCATE_MODE[element_name] = (by_method, element_value)

# 打印字典中的所有元素和对应的定位方式和元素值
for element_name, (by_method, element_value) in LOCATE_MODE.items():
    log = f"元素名称: {element_name}, 定位方式: {by_method}, 元素值: {element_value}"


def pop_by(element):
    by_method, element_value = LOCATE_MODE[element]
    return by_method, element_value


def logger_element():
    return log

# 如需调试以下if代码进行测试，第四行代码yaml文件路径须改为上级目录即../,使用runner.py时请改为当前目录即./
if __name__ == '__main__':
    by_method, element_value = pop_by('账号框')
    print(by_method, element_value)
