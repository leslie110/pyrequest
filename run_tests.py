# conding=utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest,time,os
from db_fixture import test_data

# 指定测试用例为当前文件夹下的interface目录
dir = os.path.dirname(__file__)
test_dir = dir + "/interface"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="*_test.py")

if __name__ == '__main__':
    test_data.init_data()  # 初始化接口数据

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = dir + "/report/" + now + "_result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='我的测试报告',
                            description='测试用例执行情况')
    runner.run(discover)
    fp.close()
