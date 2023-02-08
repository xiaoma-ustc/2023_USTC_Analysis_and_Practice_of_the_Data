import scrapy
from mySpider.items import MyspiderItem

class PojSpider(scrapy.Spider):
    name = "poj"
    allowed_domains = ["poj.org"]
    start_urls = ["http://poj.org/problemlist"]
    count = 0

    def parse(self, response):
        for flag in range(2, 102):
            
            
            next_href = '/html/body/table[2]/tr['+ str(flag) + ']/td[2]/a/@href'
            next_url = 'http://poj.org/' + response.xpath(next_href).extract_first()
            print(next_url)
            yield scrapy.Request(url = next_url, callback=self.DetailParse)
            flag += 1 
        if(self.count == 1):
            return
        next_href = '/html/body/center/a[2]/@href'
        next_url = 'http://poj.org/' + response.xpath(next_href).extract_first()
        self.count += 1
        yield scrapy.Request(url = next_url, callback=self.parse)
        
            

    def DetailParse(self, response):
        item = MyspiderItem()
        print("!!!!!!!")
        item['Title'] = response.xpath('/html/body/table[2]/tr/td/div[2]/text()').extract()
        item['TimeLimit'] = response.xpath('/html/body/table[2]/tr/td/div[3]/table/tr[1]/td[1]/text()').extract()
        item['MemoryLimit'] = response.xpath('/html/body/table[2]/tr/td/div[3]/table/tr[1]/td[3]/text()').extract()
        item['TotalSubmissions'] = response.xpath('/html/body/table[2]/tr/td/div[3]/table/tr[2]/td[1]/text()').extract()
        item['Accepted']  = response.xpath('/html/body/table[2]/tr/td/div[3]/table/tr[2]/td[3]/text()').extract()
        item['Description']  = response.xpath('/html/body/table[2]/tr/td/div[4]/text()').extract()
        item['Input'] = response.xpath('/html/body/table[2]/tr/td/div[5]/text()').extract()
        item['OutPut'] = response.xpath('/html/body/table[2]/tr/td/div[6]/text()').extract()
        item['SampleInput'] = response.xpath('/html/body/table[2]/tr/td/pre[1]/text()').extract()
        item['SampleOutput'] = response.xpath('/html/body/table[2]/tr/td/pre[2]/text()').extract()
        item['Hint'] = response.xpath('/html/body/table[2]/tr/td/div[7]/text()').extract()
        item['Source'] = response.xpath('/html/body/table[2]/tr/td/div[8]/a/text()').extract()
        
        
        
        yield item