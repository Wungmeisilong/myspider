# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道文件，编写数据处理的代码
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MyspiderPipeline:
    def __init__(self):
        self.file = open("items.json", "w", encoding="utf-8")
    def process_item(self, item, spider):
        # 处理每个item
        # print(item)
        json_data = json.dumps(item, ensure_ascii=False)
        self.file.write(json_data + ",\n")

        return item
    
    def close_spider(self):
        self.file.close()
