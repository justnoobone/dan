# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains


def actions(driver):
    actions = ActionChains(driver)
    return actions