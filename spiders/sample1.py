from pathlib import Path
from scrapy.selector import Selector
from urllib.parse import urljoin

import scrapy


class Sample1Spider(scrapy.Spider):
    name = "sample1"

    def start_requests(self):
        yield scrapy.Request(url="https://www.srmonline.in/", callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"home.html"
        # Path(filename).write_bytes(response.body)

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

        # base_url = 'https://www.example.com/'
        # relative_url = '/about.html'
        # absolute_url = urljoin(base_url, relative_url)
        # print(absolute_url)

        # next_page = response.xpath("//div[@class = 'mobile']/div/div/nav[@class='mainMenu']/ul[@class='nav1']").get()
        # next_page = response.css(
        #     "div.mobile div div nav.mainMenu ul.nav1 li ul li a::attr(href)").getall()

        # if next_page[1] is not None:
        # yield response.follow('Apex_leadership', callback=self.apex_details)
        # In the above code, response.follow() creates a new Request object to follow the link /Apex_leadership relative to the current response
        # response.follow_all(): This method is similar to response.follow(), but it takes a list of links instead of a single link.
        # yield scrapy.Request(next_page[1], callback=self.apex_details)

        # spider arguments "https://docs.scrapy.org/en/latest/intro/tutorial.html#using-spider-arguments"
        url = "https://www.srmonline.in/" + getattr(self, 'tag', None)
        print(url)
        if url is not None:
            yield scrapy.Request(url, callback=self.apex_details)

    def apex_details(self, response):
        filename = f"apex.html"
        Path(filename).write_bytes(response.body)
