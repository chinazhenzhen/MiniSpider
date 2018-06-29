# -*- coding: UTF-8 -*-
"""读取种子文件"""


import config_load
import scan_log


class SeedFileLoad(object):
    """读取种子文件"""
    config = config_load.ConfigLoad()
    seed_file_path = config.url_list_file

    @classmethod
    def load_seed_file(cls):
        """
        将种子文件中的所有url保存下来，用list传递出去
        :return list:返回的种子文件中的url列表
        """
        try:
            with open(cls.seed_file_path, 'r+') as my_file:
                file_list = []
                for line in my_file.readlines():
                    file_list.append(line.strip('\n'))
        except Exception as e:
            scan_log.ScanLog.scan_err(str(e)+"-->该文件打不开或者不存在:" + cls.seed_file_path)

        return file_list
