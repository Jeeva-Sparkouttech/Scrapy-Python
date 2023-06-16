import scrapy
import json
from ..items import userData

class ApiScrapping(scrapy.Spider):
    name = "apiscrap"
    headers = {'Authorization': 'Bearer 2c8ce3da4390b387:003dd62a6b1af7fb5f7c10a09a0d4f64b16dc40786e4e5379e96ce6e26254afc91f850474c5af36bffedddadab2d04363c59497bf870045d053ebe43fb6285e735621caa1ba66e1da1c7d01b825ba14c256b63b8592bf346fdb4f7df5c43d955d7bf85e66834b8cd9614e1ccce414b23f84654385e8cef3c60b2db2369b69064c4a9b5c809c37703a3a1db8d77f57b27a58632d2f9c139e414b7022f289a564697e5cb9eaa40f8e343fef489150db50cceee1cc8f366faad45d493d7ba1f3943bfc32f45f747ff04c3dbf119ccc2b267e59f05d2fda1cb80b3d20ed996377ffa'}
    allowed_domains = [""]
    start_urls = [""]

    def start_requests(self):
        yield scrapy.Request(url="http://3.129.6.80:3000/api/v1/admin/list-user", headers=self.headers, callback=self.parse)

    def parse(self, response):
        json_response = json.loads(response.body)
        # json_response = json_response.get('data') # accessing the data from response.body
        Item = userData()
        Item['name'] = json_response.get('data')[0].get('full_name')
        Item['email'] = json_response.get('data')[0].get('email')
        Item['walletAddress'] = json_response.get('data')[0].get('wallet_address')
        # print(Item.keys())
        # print(Item.items())
        # Item2 = Item.copy()
        # print(Item2.items())
        yield Item
