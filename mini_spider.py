# -*- coding: UTF-8 -*-
"""
主程序
使用说明：
启动： python mini_spider.py -c spider.conf
日志文件： my.log
配置文件： spider.conf
单元测试： my_unittest.py
磁盘储存： output文件夹

程序思路：
用set储存所有的url，进行去重处理
用queue储存某一层的url进行处理
bfs广度搜索，到达深度，函数退出，程序结束。
生产者消费者模式
串行生产一整层的url，消费者并发处理一整层的url
----------------------------------------
bug:由于文件名处理正斜杠有点问题，这里用#号替代正斜杠。保存在output中
----------------------------------------
"""

import argparse


import crawl_data
import scan_log

if __name__ == "__main__":
    print "程序运行中。。。"

    parser = argparse.ArgumentParser(description=
                                     "This is a mini_spider Author: mazhen04,"
                                     "详情请看mini_spider.py中的注释")
    parser.add_argument('--verbose', '-v', action='store_true', help='which version ?')
    parser.add_argument('-c', required=True, help="select spider-config file.")

    args = parser.parse_args()
    if args.verbose:
        print "mini-spider v1.0"
    if args.c:
        # 把配置文件的文件路径写在一个文件里，读取文件路径的时候直接访问文件即可。
        try:
            with open('./config_filename', 'w+') as my_file:
                my_file.write(args.c)
        except Exception as e:
            scan_log.ScanLog.scan_err(str(e)+"-->该文件打不开或者不存在:" + './config_filename')

        d = crawl_data.CrawlData()
        d.bfs()

    print "程序运行结束。。。日志文件保存在my.log  &  my.log.wf"
