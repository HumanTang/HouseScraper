from pathlib import Path
from urllib.parse import unquote
import scrapy
import re
import json
from HouseScraper.items import Property

class QuotesSpider(scrapy.Spider):
    name = "main"

    def start_requests(self):
        urls = [
            "https://www.e-uchina.net/api/search?searchType=house&priceLow=2500&priceHigh=8000&kenchiku=3&mode=bukken&sort=video&perPage=50&other_options=has_pic&page=1",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        res = jsonresponse["data"]
        a = res["bukkens"]["data"]
        length = len(res["bukkens"]["data"])
        for i in range(0, length):
            doc = Property()
            doc["price"] = a[i]["price_sort"]
            doc["price_text"] = a[i]["price_disp"]
            doc["title"] = a[i]["bukken_name_ka"]
            doc["address"] = a[i]["address_disp"]
            doc["transport"] = a[i]["transport_info"]
            link = a[i]["permalink"]
            yield scrapy.Request(url=link, callback=self.parseDoc, meta={'doc': doc})
        next_page_url = res["bukkens"]["next_page_url"]
        if (next_page_url is not None):
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parseDoc(self, response):
        doc = response.meta.get('doc')
        # print(item)
        page = response.url
        url = unquote(page)
        # doc = Property()
        # print(response.body)
        names = response.css('h1 span.detail-bukken-text::text').get()
        property_type = response.css('h1 span.detail-bukken-type::text').get()
        price = response.css('div.bukken-info th:contains("価格") + td::text').get()
        address = response.css('div.bukken-info th:contains("所在地") + td::text').get()
        transport = response.css('div.bukken-info th:contains("交通") + td::text').get()
        year_built = response.css('div.bukken-info th:contains("築年月") + td::text').get()
        floorplan = response.css('div.bukken-info th:contains("間取り") + td::text').get()
        area = response.css('div.bukken-info th:contains("専有面積") + td::text').get()
        build_area = response.css('div.bukken-info th:contains("建物面積") + td::text').get()
        land_area = response.css('div.bukken-info th:contains("土地面積") + td::text').get()
        floor = response.css('div.bukken-info th:contains("階数") + td::text').get()
        land_type = response.css('div.bukken-info th:contains("地目") + td::text').get()
        images = response.css('#lightgallery a img::attr(src)').getall()

        doc['images_url'] = {}

        # #print(str(names))
        # #print(price)

        # transport = transport.replace(" ","").replace("\\n","").strip()
        # translated = translator.translate(str(transport, dest='zh-tw')

        doc['url'] = unquote(response.url)
        doc['title'] = names

        doc['images_url'] = images
        doc['room'] = floorplan

        doc['floor'] = floor
        doc['land_type'] = land_type
        doc['property_type'] = property_type

        if (year_built is not None):
            doc['year_built'] = year_built
        else:
            doc['year_built'] = 0

        doc['floorplan'] = floorplan
        if (area is not None):

            doc['area'] = area
        else:
            area = 0

        if (build_area is not None):
            doc['build_area'] = build_area
        else:
            doc['build_area'] = 0

        if (land_area is not None):
            doc['land_area'] = land_area
        else:
            doc['land_area'] = 0

        if (floorplan is not None):
            floorplan = room(floorplan)

        yield doc
        # filename = '%s.html' % url
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

def room(floorplan):
    if (floorplan == "ワンルーム"):
        # print('one room')
        return 1
    elif (floorplan.find("K") != -1):
        fp = floorplan.split("K")
        fp[0] = re.sub("[^\d\.]", "", fp[0])
        # print('%d room' % int(fp[0]))
        f = int(fp[0])
        return f
    else:
        return 0

def hkd(price):
    hkd = float(price) * 0.071 / 10 ** 4
    # print('hkd: %.2f' % round(hkd,2))
    return round(hkd, 2)