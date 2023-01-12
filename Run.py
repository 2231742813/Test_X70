# -*- coding: UTF-8 -*-
import pytest
import os
import time

if __name__ == '__main__':

    pytest.main(["-sv", "--alluredir" , "./report/temp_json_report"])
    time.sleep(3)
    os.system("allure generate ./report/temp_json_report -o ./report/html --clean")
    # 1231231111
