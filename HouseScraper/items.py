# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Property(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    price_text = scrapy.Field()
    address = scrapy.Field()
    transport = scrapy.Field()
    images_url = scrapy.Field()
    images_floorplan = scrapy.Field()
    year_built = scrapy.Field()
    floorplan = scrapy.Field()
    area = scrapy.Field()
    build_area = scrapy.Field()
    land_area = scrapy.Field()
    man_fee = scrapy.Field()
    repair_fee = scrapy.Field()
    floor = scrapy.Field()
    land_type = scrapy.Field()
    status = scrapy.Field()
    expected_return = scrapy.Field()
    property_type = scrapy.Field()
    expire   = scrapy.Field()
    region = scrapy.Field()
    pid = scrapy.Field()
    town = scrapy.Field()
    #unused field
    gross_yield = scrapy.Field()
    room = scrapy.Field()
    #new Field
    map_url = scrapy.Field()
    house_space_metr = scrapy.Field()
    tochi_space_metr = scrapy.Field()
    trade_disp = scrapy.Field()
    yoto_chiki_disp = scrapy.Field()
    city_name = scrapy.Field()
    area_name = scrapy.Field()
    house_kaisu_chijo = scrapy.Field()
    chimoku_disp = scrapy.Field()
    kozo_type_disp = scrapy.Field()
    created_at_disp = scrapy.Field()
    updated_at_disp = scrapy.Field()
    expired_at_disp = scrapy.Field()
    is_new_arrivals = scrapy.Field()
    madori_space_all = scrapy.Field()
    bukken_hid = scrapy.Field()
    bus_stop1 = scrapy.Field()
    bus_time1 = scrapy.Field()
    bus_stop2 = scrapy.Field()
    bus_time2 = scrapy.Field()
    train_station = scrapy.Field()
    train_time = scrapy.Field()
    panorama_url = scrapy.Field()
    madori_space_y01 = scrapy.Field()
    madori_space_y02 = scrapy.Field()
    madori_space_y03 = scrapy.Field()
    madori_space_y04 = scrapy.Field()
    price_max = scrapy.Field()
    thumbnail_image_url = scrapy.Field()
    madori_image_url = scrapy.Field()
    madori_image_thumbnail_url = scrapy.Field()
    kenpei_yoseki_disp = scrapy.Field()
    madori_detail_disp = scrapy.Field()
    short_parking_disp = scrapy.Field()
    bukken_type = scrapy.Field()
    kenchiku_date = scrapy.Field()
    kenchiku_disp = scrapy.Field()
    kenchiku_date_disp = scrapy.Field()