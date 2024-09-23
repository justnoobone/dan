# -*- coding: utf-8 -*-
import pytest
from utils.driver_path import VcrmFillWebDriver
from selenium import webdriver


# 测试固件
@pytest.fixture(scope="module", autouse=True)
def driver():
    # 实例化VcrmFillWebDriver对象
    driver = VcrmFillWebDriver()
    driver.get('***')

    yield driver
    # 清理操作，关闭浏览器或者进行其他清理工作
    driver.quit()

# @pytest.fixture(scope="module", autouse=True)
# def Driver():
#     absdriver = webdriver.Chrome()
#     yield absdriver
#     # 清理操作，关闭浏览器或者进行其他清理工作
#     driver.quit()
