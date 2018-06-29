# -*- coding: UTF-8 -*-
"""保存所有url的set，用set来判断是否存在，用来去重"""
import threading


class UrlSet(object):
    """
    作用：链接 crawl_data.py 与 crawl_thread.py
    """
    def __init__(self, url_set):
        self.lock = threading.Lock()
        self.url_set = url_set

    def put_set(self, url):
        """
        进行加锁处理
        :param url:
        :return:
        """
        self.lock.acquire()
        # 去重
        if url not in self.url_set:
            self.url_set.add(url)
        self.lock.release()

    def return_set(self):
        """

        :return set:
        """
        return self.url_set
