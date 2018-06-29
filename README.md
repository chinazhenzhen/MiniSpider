# MiniSpider
在调研过程中，经常需要对一些网站进行定向抓取。由于python包含各种强大的库，使用python做定向抓取比较简单。请使用python开发一个迷你定向抓取器mini_spider.py，实现对种子链接的抓取，并把URL长相符合特定pattern的网页保存到磁盘上。
程序运行: 
python mini_spider.py -c spider.conf 
配置文件spider.conf: 
[spider] 
url_list_file: ./urls ; 种子文件路径 
output_directory: ./output ; 抓取结果存储目录 
max_depth: 1 ; 最大抓取深度(种子为0级) 
crawl_interval: 1 ; 抓取间隔. 单位: 秒 
crawl_timeout: 1 ; 抓取超时. 单位: 秒 
target_url: .*.(htm|html)$ ; 需要存储的目标网页URL pattern(正则表达式) 
thread_count: 8 ; 抓取线程数 
