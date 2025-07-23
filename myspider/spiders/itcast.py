import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"     # 爬虫名
    allowed_domains = ["itheima.com"] # 允许爬取的域名
    start_urls = ["https://www.itheima.com/teacher.html"] # 起始URL

    def parse(self, response): # 响应处理方法，通常用于解析响应内容
        # 定义对于响应的处理逻辑
        # with open('itcast.html','wb') as f:
        #     f.write(response.body)
        #获取所有节点
        node_list = response.xpath("//div[@class='li_txt']")

        for node in node_list:
            #获取节点中的数据
            temp = {}

            temp['name'] = node.xpath('./h3/text()').get()
            temp['title'] = node.xpath('./h4/text()').get()
            temp['info'] = node.xpath('./p/text()').get()

            yield temp  # 使用yield返回数据，Scrapy会自动处理数据的存储
            