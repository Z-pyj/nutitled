import scrapy


# TODO:爬取内容并解析结果，这个类必现继承scrapy.Spider
class QuotesSpider(scrapy.Spider):
    # 每个项目唯一的名字，用来区分不同的Spider
    name = 'quotes'
    # 允许爬取的域名
    allowed_domains = ['quotes.toscrape.com']
    # spider启动时爬取的url列表，初始请求是由它定义的
    start_urls = ['https://quotes.toscrape.com/']
    # 默认start_urls链接请求完成下载后，parse方法就会被调用，返回的响应作为唯一的参数传递给parse方法
    # 该方法解析返回的响应、提取数据或者进一步生成要处理的请求
    def parse(self, response):
        pass
