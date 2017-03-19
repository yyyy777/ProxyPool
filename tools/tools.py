# coding=utf-8
# !usr/bin/python3

import requests
import re
import functools
from lxml import etree as ET
from .useragent import header
import logging
from logging.handlers import TimedRotatingFileHandler

# https://docs.python.org/3.5/library/logging.html,python日志级别


CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


def crawlProxy(func):
    '''
    抓取代理的装饰器，方便输出错误信息
    :param func:
    :return:
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('抓取代理ip失败:%s', e)
    return wrapper


def verifyProxy(proxy):
    '''
    检查代理ip的格式是否正确
    :param proxy:
    :return:
    '''
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    return True if re.findall(verify_regex, proxy) else False


def getHtmlTree(url, xpath=True, **kwargs):
    '''
    获取免费代理ip页面的html树用于解析
    :param url:
    :param kwargs:
    :return:
    '''
    if xpath:
        html = requests.get(url=url, headers=header, timeout=30).content
        return ET.HTML(html)
    else:
        html = requests.get(url=url, headers=header).content
        return html


class LogHandler(logging.Logger):

    def __init__(self, name, level=DEBUG):
        '''
        初始化
        :param name: 
        :param level: 
        '''
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=self.level)
        self.__setFileHandler__()
        self.__setStreamHandler__()

    def __setFileHandler__(self, level=None):
        '''
        setFileHandler
        :param level:
        :return:
        '''
        file_name = '../log/%s' % self.name
        # https://docs.python.org/3.5/library/logging.handlers.html?highlight=streamhandler#timedrotatingfilehandler
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(
            filename=file_name, when='D', interval=1, backupCount=15)
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        setStreamHandler
        :param level:
        :return:
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

'''
if __name__ == '__main__':
    log = LogHandler('test')
    log.info('this is a test msg')
    pass
'''