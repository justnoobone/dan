本次测试使用pytest搭建自动化框架，修改按照第7修改后可以直接runner.py文件进行测试，测试网址为百度
运行本测试框架需要命令行输入以下内容
pip install pytest / pip3 install pytest
pip install yaml  / pip3 install PyYAML
pip install selenium / pip3 install selenium
pip install pywinauto /pip3 install pywinauto
测试框架解释如下：
1.page目录中是对selenium方法的封装，无必要不改动
2.page_element目录是对页面元素的封装,后续页面元素的增加都要在本目录中进行
本目录中元素的名称为搜索框，定位方式为By.ID,属性值为pw，将写为
搜索框:
  By: 'id'
  element: 'kw'
其他定位方式参考
    'id': By.ID,
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'class': By.CLASS_NAME,
    'text': By.LINK_TEXT
3.page_object目录是对编写元素定位以及方法的编写
4.testCase目录是存放测试用例的目录，新建测试文件时请按照test_case*进行命名，其中的测试方法请使用test_开头
5.testData目录是存放参数化文件的目录，有可能用到的场景有登录时对账户和密码的参数化测试
6.utils目录存放的是工具类，driver_path.py文件定义了浏览器驱动和隐式等待。
extract_element.py文件中封装了元素提取的方法，实现了将find_element(By.ID,'id')中的元素提取，今后的元素定位代码将直接使用find_element(element)进行元素定位
7.conftest.py文件中定义了测试的启动项。
需要改动浏览器驱动对象的位置以及网站的位置请在conftest.py中进行改动
8.pytest.ini文件中是测试套件，今后用于对测试用例的标签化执行
9.runner.py文件是自动化测试的执行入口，后续测试用例的执行方式在本文件进行修改
