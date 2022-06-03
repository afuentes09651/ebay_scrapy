import scrapy
import csv
import os
import datetime

class JobSpider(scrapy.Spider):
    name = 'bids'

    #ok so maybe it isn't a bid to start but oh well
    start_urls =[
    'https://www.ebay.com/itm/143584328286?hash=item216e4afa5e:g:AWIAAOSwOL9em4jw',
    'https://www.ebay.com/itm/265221026953?hash=item3dc067b489:g:FWIAAOSwikBg5LZI',
    'https://www.ebay.com/itm/275135047675?hash=item400f53a7fb:g:pUgAAOSwA~Nh7jPI',
    'https://www.ebay.com/itm/225015668326?hash=item3463fa9e66:g:2pwAAOSwaalimQvu',
    ]

    def parse(self, response):
        file_name = 'ebay.csv'

        if os.path.exists(file_name):
            out_file = open(file_name,'a')
            csv_writer = csv.writer(out_file)
        else:
            out_file = open(file_name,'w')
            csv_writer = csv.writer(out_file)
            csv_writer.writerow(['name','price', 'seller']) #make the header row for the col names

        #Values Needed
        name = response.xpath('//title/text()').get().replace(" | eBay",'')
        seller = response.css('button.follow-ebay.follow-ebay-fakeLink.nounderline.btn.btn--fake-link.btn--large.btn--primary::attr(aria-label)').get().replace('Save seller ', '')
        price = response.xpath('//span[@itemprop="price"]/text()').get()

        csv_writer.writerow([name,price,seller])
        out_file.close()

        return None
