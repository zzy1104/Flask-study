# -*- coding:utf-8 -*-

import io
import os
import sys
from time import sleep
import urllib
import json
from flask import Flask
# 导入线程模块
import threading


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 主程序在这里
if __name__ == "__main__":

    # 开启 flask 服务
    app.run()
