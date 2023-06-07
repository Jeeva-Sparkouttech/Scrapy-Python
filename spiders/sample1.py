from pathlib import Path
from scrapy.selector import Selector

import scrapy


class Sample1Spider(scrapy.Spider):
    name = "sample1"

    def start_requests(self):
        yield scrapy.Request(url="https://www.srmonline.in/", callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        filename = f"sample-1.html"
        Path(filename).write_bytes(response.body)

        # print(response.css('title::text').get())
        # print(response.xpath('//title/text()').get())
        # response.css('div.classname::text').getall()

        # for data in response.css("button.ruttl-animate::text").getall():
        #     yield dict(type = data)

        # body = "<html><body><h5>scrapy</span></h5></html>"
        # print(Selector(text=body).xpath("//h5/text()").get())

        # print(response.css("h5").xpath("//a/@href").get())
        # print(response.xpath("//div[@id='studentlogin']/div/div/div/h5/text()").get())
        # print(response.css("div.mobile div.mainContainer div a::attr(href)").get())
        # print(response.css("div.mobile div.mainContainer div a").attrib['href'])

        # next_page = response.xpath("//div[@class = 'mobile']/div/div/nav[@class='mainMenu']/ul[@class='nav1']").get()
        next_page = response.css(
            "div.mobile div div nav.mainMenu ul.nav1 li ul li a::attr(href)").getall()
        if next_page[1] is not None:
            yield scrapy.Request(next_page[1], callback=self.parse)
