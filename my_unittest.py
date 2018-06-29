# -*- coding: UTF-8 -*-
"""
单元测试
"""
import unittest


import webpage_request_parse
import config_load
import seedfile_load
import url_set


class TestWebPageRequestParse(unittest.TestCase):
    """Test webpage_request_parse.py"""

    test_dict = {
        "simple_url": "pycm.baidu.com:8081/",
        # simple_url返回的URL的set,即simple_url页面包含5个不同的url链接。
        "simple_url_set": 5,
        "404_url": "pycm.baidu.com:8081/page4.html",
    }

    def test_get_url_information(self):
        """test get_url_information"""
        test_object = webpage_request_parse.WebPageRequestParse(self.test_dict["simple_url"])
        self.assertEqual(5, len(test_object.get_url_information()))

    def test_to_request_404(self):
        """test to_request 404"""
        test_object = webpage_request_parse.WebPageRequestParse(self.test_dict["404_url"])
        # 当页面为404时，返回空的字符串
        self.assertEqual("", test_object.to_request())


class TestConfigLoad(unittest.TestCase):
    """Test config_load.py"""

    test_dict = {
        "url_list_file": "./urls",
    }

    def test_configload(self):
        """Test ConfigLoad"""
        config = config_load.ConfigLoad()
        self.assertEqual(self.test_dict["url_list_file"], config.url_list_file)


class TestSeedfileLoad(unittest.TestCase):
    """Test seedfile_load"""

    test_dict = {
        "path": "./urls",
    }

    def test_seed_file_load(self):
        """Test seedfileload"""
        test_object = seedfile_load.SeedFileLoad()

        with open(self.test_dict["path"], 'r+') as my_file:
            file_list = []
            for line in my_file.readlines():
                file_list.append(line.strip('\n'))

        self.assertEqual(len(file_list), len(test_object.load_seed_file()))


class TestUrlSet(unittest.TestCase):
    """Test url_set.py"""

    # noinspection PySetFunctionToLiteral
    test_set = set(["url1", "url2", "url3"])
    test_object = url_set.UrlSet(test_set)

    def test_url_set_return(self):
        """Test urlSet   return_set"""
        return_set = self.test_object.return_set()
        # set正常返回
        self.assertEqual(True, self.test_set == return_set)


if __name__ == '__main__':
    unittest.main()

