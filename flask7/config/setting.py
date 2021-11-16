"""
    localsetting导入成功会覆盖此文件中相同的项
    此文件一般导入公共并且不重要的内容
    或者非本地调试的公用的非保密的配置
"""


DB_HOST = "xxx"


try:
    from flask7.config.localsetting import *
except ImportError:
    pass