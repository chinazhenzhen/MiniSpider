# -*- coding: UTF-8 -*-
""" 实现抓取线程 """
import threading
import webpage_request_parse
import url_set
import Queue


import config_load

g_queue = Queue.Queue()



class CrawlThread(threading.Thread):
    """
    简单的生产者消费者模式；
    bfs将每层的url生产出来，然后在这个类中的消费者开启多线程进行处理。
    """
    config = config_load.ConfigLoad()

    def __init__(self, queue, my_url_set):
        """
        引用queue的作用是为了更好的进行线程间的通讯
        :param queue:
        :param my_url_set:
        """
        #g_queue.join()
        super(CrawlThread, self).__init__()
        self.queue = Queue.Queue()

        while queue.empty() is not True:
            self.queue.put(queue.get())

        self.save_set = url_set.UrlSet(my_url_set)

    def work(self, url):
        """
        处理url的函数
        :param url:
        """
        work_class = webpage_request_parse.WebPageRequestParse(url).get_url_information()
        for url in work_class:

            self.save_set.put_set(url)

    def consumer_url(self):
        """
        消费者处理url函数，每个线程的得到url会被分配到这个地方。
        :return:
        """
        while g_queue.empty() is not True:
            url = g_queue.get()
            #scan_log.ScanLog.scan_info("正在处理-->" + url)
            self.work(url)
            #scan_log.ScanLog.scan_info("处理完成-->" + url)
            g_queue.task_done()

    def start_threading(self):
        """
        开启多线程
        """

        while self.queue.empty() is not True:
            g_queue.put(self.queue.get())

        for thread_one in range(0, self.config.thread_count):
            one_thread = threading.Thread(target=self.consumer_url)
            one_thread.start()

    def return_get_url_set(self):
        """
        消费者将所有url处理完之后，最后再将处理好的urlset传回
        :return set:
        """
        g_queue.join()
        return self.save_set.return_set()
