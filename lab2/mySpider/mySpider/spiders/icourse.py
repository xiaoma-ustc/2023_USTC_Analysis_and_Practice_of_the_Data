import scrapy
from mySpider.items import MyspiderItem

class IcourseSpider(scrapy.Spider):
    name = "icourse"
    allowed_domains = ["icourse.club"]
    start_urls = ["https://icourse.club/course/"]
    count = 2
    num = 0

    def parse(self, response):
        for i in range(2,12):
            next_href = '/html/body/div[1]/div[3]/div/div[3]/div/div[' + str(i) +']/div/div/a/@href'
            print(response.xpath(next_href).extract_first())
            next_url = 'https://icourse.club' + response.xpath(next_href).extract_first()
            print(next_url)
            yield scrapy.Request(url= next_url, callback=self.DetailParse)
        if self.count == 21:
            return
        next_url = 'https://icourse.club/course/?page=' + str(self.count)
        self.count += 1
        yield scrapy.Request(url = next_url, callback=self.parse)
        
    def DetailParse(self, response):
        item = MyspiderItem()
        t1 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/span[1]/text()').extract()
        t2 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/span[2]/text()').extract()
        t3 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/ul/li[1]/text()').extract()
        t4 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/ul/li[2]/text()').extract()
        t5 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/ul/li[3]/text()').extract()
        t6 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/ul/li[4]/text()').extract()
        t7 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[1]/td[1]/text()').extract()
        t8 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[1]/td[2]/text()').extract()
        t9 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[2]/td[1]/text()').extract()
        t10= response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[2]/td[2]/text()').extract()
        t11 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[3]/td[1]/text()').extract()
        t12 = response.xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[3]/td[2]/text()').extract()
        item['序号'] = self.num
        if len(t2) == 0:
            item['课程名称'] = t1[0] + '（无教师信息）'
        else:
            item['课程名称'] = t1[0] + t2[0]
        t3 = t3[0]
        item['课程难度'] = t3[5:]
        t4 = t4[0]
        item['作业多少'] = t4[5:]
        t5 = t5[0]
        item['给分好坏'] = t5[5:]
        t6 = t6[0]
        item['收获大小'] = t6[5:]
        item['选课类别'] = t7[0]
        item['教学类型'] = t8[0]
        item['课程类别'] = t9[0]
        item['开课单位'] = t10[0]
        item['课程层次'] = t11[0]
        item['学分'] = t12[0]
        self.num += 1
        yield item