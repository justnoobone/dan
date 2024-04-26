# -*- coding: utf-8 -*-
from page.webdriver import LocalWebDriver


class VcrmFillWebDriver(LocalWebDriver):
    def __init__(self, implicitly_wait=20):
        super().__init__()
        self.implicitly_wait_time = implicitly_wait
        self.maximize_window()