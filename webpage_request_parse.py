# -*- coding: UTF-8 -*-
"""
对url进行请求和解析
"""
import urllib2
import re


import config_load
import webpage_save
import scan_log


class WebPageRequestParse(object):
    """
    url请求和解析类
    """
    def __init__(self, url):

        self.url = self.reduce_http_https_ftp(url)

        self.headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        self.config = config_load.ConfigLoad()

    # 请求网页得到网址
    def to_request(self):
        """
        请求
        :return data-url请求得到的页面源代码:
        """
        the_request_url = "http://" + self.url
        the_request = urllib2.Request(url=the_request_url, headers=self.headers)
        # 404
        try:
            request_er = urllib2.urlopen(the_request, timeout=self.config.crawl_timeout)
        except Exception as e:
            scan_log.ScanLog.scan_err(str(e)+"-->error url:" + the_request_url)
            return ''
        # GBK
        try:
            data = request_er.read().encode('utf8')
        except Exception as e:
            scan_log.ScanLog.scan_info(str(e) + "-->GBK url:" + the_request_url)
            request_er = urllib2.urlopen(the_request)
            data = request_er.read()
        # 将页面写入到文件
        webpage_save.SaveFile.save_file(self.url, data)

        return data

    def get_url_information(self):
        """
        将某个 url 页面中的url提取出来，通过set返回。
        :return set:
        """
        data = self.to_request()
        regular = re.compile(self.config.target_url)
        result = []
        for one in regular.findall(data):
            result.append(self.completed_url(one))

        return set(result)

    def completed_url(self, url):
        """
        url处理
        :param url:
        :return 处理后的url:
        """
        if "http" in url:
            pass
        else:
            if '/' not in url:
                url = self.url + '/' + url
            else:
                if "//" in url:
                    tmp = ''
                    url = tmp + url[2:]
                else:
                    tmp = ''
                    url = tmp + url[:-1]

        return url

    @staticmethod
    def reduce_http_https_ftp(url_str):
        """去掉url的http https的头"""
        if "http://" in url_str:
            url_str = url_str[7:]
        if "https://" in url_str:
            url_str = url_str[8:]

        return url_str
