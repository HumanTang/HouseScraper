from pathlib import Path
from urllib.parse import unquote
import scrapy
import re
import json
from HouseScraper.items import Property
from HouseScraper.items import Property
class GooHomeSpider(scrapy.Spider):
    name = "goohome"

    def start_requests(self):
        urls = [
            "https://goohome.jp/kodate/cities/?chiku=5&page=1-100"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        baseurl = "https://goohome.jp/"
        page_list = response.css('.detail_view_btn a::attr(href)').getall()
        print(page_list)
        for page in page_list:
            # page = str(page)
            detail_page = page
            print(detail_page)
            yield scrapy.Request(baseurl + detail_page, callback=self.detail_parse)


           # next_page = response.response.css('//a[contains(text(),"次へ")]/@href').getall()
           # if next_page is not None:
           #     print("next_page" + next_page)
           #     yield scrapy.Request(baseurl + next_page, callback=self.next_parse)
    def detail_parse(self, response):
        homebaseurl = "https://goohome.jp/"
        print("detail_parse")
        page = response.url
        url = unquote(page)
        doc = Property()
        names = response.css('#main_clm1 > h2::text').get()
        property_type = response.css('#detail_pd > table.table_top th:contains("用途地域") + td::text').get()
        price = response.css('#detail_pd > table.table_top th:contains("価格") + td::text').get()
        address = response.css('#detail_pd > table.table_top th:contains("所在地") + td::text').get()
        transport = response.css('#detail_pd > table.table_top th:contains("交通") + td::text').get()
        year_built = response.css('#detail_pd > table.table_top th:contains("築年月") + td::text').get()
        floorplan = response.css('#detail_pd > table.table_top th:contains("間取り") + td::text').get()
        area = response.css('#detail_pd > table.table_top th:contains("専有面積") + td::text').get()
        build_area = response.css('#detail_pd > table.table_top th:contains("建物面積") + td::text').get()
        land_area = response.css('#detail_pd > table.table_top th:contains("土地面積") + td::text').get()
        floor = response.css('#detail_pd > table.table_top th:contains("階数") + td::text').get()
        land_type = response.css('#detail_pd > table.table_top th:contains("地目") + td::text').get()
        images = response.css('#lightgallery li img::attr(data-src)').getall()

        doc['title'] = names
        doc['price'] = price
        doc['address'] = address.strip()
        doc['transport'] = transport.strip()
        doc['images_url'] = {}
        doc['images_url'] = images
        doc['url'] = unquote(response.url)
        doc['images_url'] = images
        print(images)
        doc['room'] = floorplan
        doc['floor'] = floor
        doc['land_type'] = land_type
        doc['property_type'] = property_type
        doc['pid'] = response.url.split('/')[-1]
        doc['floorplan'] = floorplan

        if (year_built is not None):
            doc['year_built'] = year_built
        else:
            doc['year_built'] = 0

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

        yield doc