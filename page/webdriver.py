# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.extract_element import pop_by


class LocalWebDriver(webdriver.Chrome):
    def __init__(self):
        super().__init__()

    def get_element(self, element):
        # 调用pop_by函数并返回定位方式和元素值
        by_method, element_value = pop_by(element)
        return by_method, element_value

    def find_element(self, method, element, text=None):
        # 获取定位方式和元素值
        by_method, element_value = self.get_element(element)
        # 使用获取到的定位方式和元素值来查找元素
        if method == '':
            time.sleep(2)
            return super().find_element(by_method, element_value)
        elif method == 'presence':
            return WebDriverWait(super(), 20, 1).until(EC.presence_of_element_located((by_method, element_value)))
        elif method == 'clickable':
            return WebDriverWait(super(), 20, 1).until(EC.element_to_be_clickable((by_method, element_value)))
        elif method == 'visibility':
            return WebDriverWait(super(), 20, 1).until(EC.visibility_of_element_located((by_method, element_value)))
        elif method == 'text':
            return WebDriverWait(super(), 20, 1).until(
                EC.text_to_be_present_in_element((by_method, element_value), text))
        else:
            return print(f'{element}定位信息有误')


# 使用示例
if __name__ == '__main__':
    driver = LocalWebDriver()
    driver.get('https://sit1.vcrm.vip:9000/')
    try:
        element = driver.find_element('presence', '账号框')
        element.send_keys('123')
        time.sleep(2)
    except Exception as e:
        print(f"查找元素时出错: {e}")
    finally:
        driver.quit()
