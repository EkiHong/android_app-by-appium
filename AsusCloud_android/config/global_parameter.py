# coding:utf-8
__author__ = 'Eki'

'''
description:配置全域變數
'''

import time
import os
import sys
project_path = (os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
test_case_path = project_path + "\\src\\test_case\\"
report_path = project_path + "\\report\\"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())
