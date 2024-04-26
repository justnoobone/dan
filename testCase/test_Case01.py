import allure
import pytest
from pageElement.creatUnit import creatUnit
from utils.get_csv_testData import get_csv_test_data
from pageElement.creatUnit import login

@pytest.mark.test
@pytest.mark.parametrize(
    'mechanismCode, repairShopCode, factoryName, typeName, factoryContact, phone, adress, contributing,city',
    get_csv_test_data(r'D:\Project\Dan\testData\导入.csv'))
def test_import_costomer(mechanismCode, repairShopCode, factoryName, typeName, factoryContact, phone, adress, contributing,city, driver):
    login(driver)
    creatUnit(mechanismCode, repairShopCode, factoryName, typeName, factoryContact, phone, adress, contributing, city, driver)
