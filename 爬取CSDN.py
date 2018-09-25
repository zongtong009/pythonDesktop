
import scrapy
class GanjiSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ['http://bj.ganji.com/fang1/chaoyang/']
 
    def parse(self,reponse):
        print (reponse)
        # 租金
        money_list = reponse.xpath(".//*[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        
        #通过 scrapy crawl zufang 打印租金
        print (title_list)