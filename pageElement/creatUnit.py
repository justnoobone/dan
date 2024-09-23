import time
from selenium.webdriver import Keys, ActionChains


def login(driver):
    driver.find_element('visibility','账号').send_keys('***')
    driver.find_element('visibility', '密码').send_keys("***")
    appear = driver.find_element('', '验证成功')

    while appear:
        if '验证成功' in appear.text:
            driver.find_element('', '登录按钮').click()
            break
        else:
            continue

    time.sleep(5)
    print('进入设置中心')
    driver.find_element('visibility', '设置中心').click()
    driver.find_element('visibility', '合作单位').click()
    driver.find_element('visibility', '创建合作单位').click()







def creatUnit(mechanismCode, repairShopCode, factoryName, typeName, factoryContact, phone, adress, contributing, city, driver):
    driver.find_element('visibility', '机构码').send_keys(mechanismCode)
    driver.find_element('visibility', '合作单位代码').send_keys(repairShopCode)
    driver.find_element('visibility', '合作单位名称').send_keys(factoryName)
    driver.find_element('', '合作单位类型').click()
    if typeName == '4S店':
        ActionChains(driver).send_keys(Keys.ENTER).perform()
    else:
        ActionChains(driver).send_keys(Keys.DOWN+Keys.ENTER).perform()
    driver.find_element('visibility', '推修联系人').send_keys(factoryContact)
    driver.find_element('visibility', '联系电话').send_keys(phone)
    driver.find_element('visibility', '详细地址').send_keys(adress)
    driver.find_element('visibility', '协赔员').send_keys(contributing)
    driver.find_element('', '客服组').click()
    ActionChains(driver).send_keys(Keys.DOWN*3 + Keys.ENTER).perform()
    time.sleep(100)

    # driver.find_element('visibility', '创建').click()

    # driver.find_element('visibility', '详细地址').send_keys(mechanismCode)
    # driver.find_element('visibility', '详细地址').send_keys(mechanismCode)




