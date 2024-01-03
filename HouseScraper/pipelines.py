# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class HousescraperPipeline:
    @classmethod
    def open_spider(self, spider):
        self.file = open("%s.csv" % (spider.name), 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = [
            "url",
            "title",
            "price",
            "address",
            "transport",
            "images_url",
            "images_floorplan",
            "year_built",
            "build_area",
            "land_area",
            "floor",
            "land_type",
            "property_type",
            "pid",
            "room"
        ]
        self.exporter.start_exporting()

    # def __init__(self):

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

