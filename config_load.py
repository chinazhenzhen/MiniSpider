# -*- coding: UTF-8 -*-
""" 读取配置文件 """

import ConfigParser
import scan_log

class ConfigLoad(object):
    """
    读取配置文件类，通过相应的方法返回配置函数。
    """
    try:
        with open('./config_filename', 'r+') as my_file:
            config_file = my_file.read()
    except Exception as e:
        scan_log.ScanLog.scan_err(str(e) + "-->该文件打不开或者不存在:" + "./config_filename")

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.config_file)

    # [spider]
    # url_list_file:./urls;
    # 种子文件路径
    # output_directory:./ output;
    # 抓取结果存储目录
    # max_depth: 1;
    # 最大抓取深度(种子为0级)
    # crawl_interval: 1;
    # 抓取间隔.单位: 秒
    # crawl_timeout: 1;
    # 抓取超时.单位: 秒
    # target_url:.*.(htm | html)$; 需要存储的目标网页URL
    # pattern(正则表达式)
    # thread_count: 8;
    # 抓取线程数

    @property
    def url_list_file(self):
        """
        :return string:
        配置参数
        """
        return self.cf.get("spider", "url_list_file")

    @property
    def output_directory(self):
        """
        :return string:
        配置参数
        """
        return self.cf.get("spider", "output_directory")

    @property
    def max_depth(self):
        """
        :return string:
        配置参数
        """
        return int(self.cf.get("spider", "max_depth"))

    @property
    def crawl_interval(self):
        """
        :return string:
        配置参数
        """
        return int(self.cf.get("spider", "crawl_interval"))

    @property
    def crawl_timeout(self):
        """
        :return string:
        配置参数
        """
        return int(self.cf.get("spider", "crawl_timeout"))

    @property
    def target_url(self):
        """
        :return string:
        配置参数
        """
        return self.cf.get("spider", "target_url")

    @property
    def thread_count(self):
        """
        :return string:
        配置参数
        """
        return int(self.cf.get("spider", "thread_count"))
