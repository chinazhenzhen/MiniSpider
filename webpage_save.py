# -*- coding: UTF-8 -*-
"""
将网页保存到磁盘
"""
import os

import config_load
import scan_log



class SaveFile(object):
    """
    保存数据到磁盘
    """
    config = config_load.ConfigLoad()
    page_file_path = config.output_directory  # 得到种子文件目录
    folder = os.path.exists(page_file_path + '/')
    if not folder:
        os.makedirs(page_file_path + '/')

    @classmethod
    def save_file(cls, url, string):
        """
        bug: 带文件名带正斜杠不好处理，所以这里就用#号代替正斜杠
        :param url:
        :param string:
        """
        my_path = cls.page_file_path + '/' + url.replace('/', '#')
        try:
            with open(my_path, 'w+') as the_file:
                the_file.write(string)
                scan_log.ScanLog.scan_info("-->该网页成功存入" + url)
        except Exception as e:
            scan_log.ScanLog.scan_err(str(e)+"-->该文件打不开或者不存在:" + my_path)

