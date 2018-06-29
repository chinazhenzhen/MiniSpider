# -*- coding: UTF-8 -*-
""" 抓取的数据均在这里进行处理 """
import Queue
import time


import config_load
import seedfile_load
import crawl_thread


class CrawlData(object):
    """
    spider程序最主要的类，主要进行spider处理过程中数据的处理。
    """
    config = config_load.ConfigLoad()
    max_depth = config.max_depth

    def __init__(self):
        """
        deep = 0 第一层的深度为0
        queue存第n层所需要处理的url
        set储存所有的url，set数据结构用来进行去重
        """
        self.deep = 0
        self.queue = Queue.Queue()
        self.set = set()
        self.save_start_data()

    def save_start_data(self):
        """
        函数只是为了处理种子文件中的url，将url存入到queue与set中
        """
        for url in seedfile_load.SeedFileLoad.load_seed_file():
            self.set.add(url)

        for url in self.set:
            self.queue.put(url)

    def bfs(self):
        """
        整个程序最主要的函数 ，广度优先遍历，将n层的url出队后进行交由crawl_thread.py处理，然后返回n+1层的数据
        """
        while True:
            # 开始新的一层处理之前，进行sleep
            self.crawl_sleep()
            # 判断是否到达最大深度，到达最大深度，跳出函数，结束程序
            if self.deep > self.config.max_depth:
                break

            thread_class = crawl_thread.CrawlThread(self.queue, self.set)
            while self.queue.empty() is not True:
                self.queue.get()
            thread_class.start_threading()

            # 利用set的与或运算进行新旧数据的处理，用来保证不重用已经处理过的url
            tmp_set = set()
            tmp_set = tmp_set | self.set
            self.set = thread_class.return_get_url_set()
            tmp_set = self.set - tmp_set

            for url in tmp_set:
                self.queue.put(url)

            self.set = tmp_set | self.set
            # 每一层进行deep++
            self.deep = self.deep + 1

    @classmethod
    def crawl_sleep(cls):
        """
        sleep
        """
        time.sleep(cls.config.crawl_interval)
