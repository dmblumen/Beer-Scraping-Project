from scrapy import Spider, Request
from beer.items import BeerItem
import re

class BeerSpider(Spider):
    name = 'beer_spider'
    allowed_urls = ['https://beerconnoisseur.com/']
    start_urls = ['https://beerconnoisseur.com/search-beer']

    def parse(self,response):
        result_urls = ['https://beerconnoisseur.com/search-beer?keys=&field_beer_style_tid=All&field_state_value=All&field_country_value=United%20States&sort_by=created&sort_order=DESC&page={}'.format(x) for x in range(102)]

        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self,response):
        condensed_urls = response.xpath('//div[@class ="views-field views-field-title"]//a/@href').extract()
        full_urls = []
        for url in condensed_urls:
            full_urls.append('https://beerconnoisseur.com' + url)

        for url in full_urls:
            yield Request(url=url, callback=self.parse_detail_page)

    def parse_detail_page(self,response):
        name = response.xpath('//h1/text()').extract()
        image = response.xpath('//div[@class="field field-name-field-beer-image field-type-image field-label-hidden"]//img/@src').extract()
        brewer = response.xpath('//div[@class="field field-name-field-brewery field-type-entityreference field-label-hidden"]//a/text()').extract()
        beer_type = response.xpath('//div[@class="field field-name-field-beer-style field-type-taxonomy-term-reference field-label-hidden"]//a/text()').extract()
        release = response.xpath('//div[@class="field field-name-field-availability field-type-taxonomy-term-reference field-label-hidden"]//a/text()').extract()
        
        ###State needs the second element pulled
        state = response.xpath('//div[@class="field field-name-field-state field-type-list-text field-label-hidden"]//div/text()').extract()[1]
        
        description = response.xpath('//div[@class="field field-name-body field-type-text-with-summary field-label-above"]//p/text()').extract()
        
        ### abv needs the % sign removed
        abv_p = response.xpath('//div[@class="field field-name-field-abv field-type-text field-label-inline clearfix"]//div[@class ="field-item even"]/text()').extract()
        abv = list(map(lambda s: s.replace('%',""),abv_p))

        ibu = response.xpath('//div[@class="field field-name-field-ibus field-type-text field-label-inline clearfix"]//div[@class ="field-item even"]/text()').extract()
        serv_temp = response.xpath('//div[@class="field field-name-field-served-at field-type-text field-label-inline clearfix"]//div[@class ="field-item even"]/text()').extract()
        hops = response.xpath('//div[@class="field field-name-field-hops field-type-text field-label-inline clearfix"]//div[@class ="field-item even"]/text()').extract()
        malts = response.xpath('//div[@class="field field-name-field-malts field-type-text field-label-inline clearfix"]//div[@class ="field-item even"]/text()').extract()
        
        ### Aroma is going to require Regex
        aroma_p = response.xpath('//div[@class="views-field views-field-field-judge-aroma"]//div[@class ="field-content"]/text()').extract_first()
        aroma = re.findall('(\d+) /',aroma_p)
        
        ### Appearance is going to require Regex
        appearance_p = response.xpath('//div[@class="views-field views-field-field-judge-appearance"]//div[@class ="field-content"]/text()').extract_first()
        appearance = re.findall('(\d+) /',appearance_p)

        ### Flavor is going to require Regex
        flavor_p = response.xpath('//div[@class="views-field views-field-field-judge-flavor"]//div[@class ="field-content"]/text()').extract_first()
        flavor = re.findall('(\d+) /',flavor_p)
        ### Mouthfeel is going to require Regex
        mouthfeel_p = response.xpath('//div[@class="views-field views-field-field-judge-mouthfeel"]//div[@class ="field-content"]/text()').extract_first()
        mouthfeel = re.findall('(\d+) /',mouthfeel_p)
        ### Overall Impression is going to require Regex
        overall_impression_p = response.xpath('//div[@class="views-field views-field-field-overall-impression"]//div[@class ="field-content"]/text()').extract_first()
        overall_impression = re.findall('(\d+) /',overall_impression_p)
        
        brewer_intro = response.xpath('//div[@class="views-field views-field-field-brewery-introduction"]//p/text()').extract_first()

        ### Review is going to require certain codes to be stripped, then creating one list with one element
        if response.xpath('//div[@class="views-field views-field-body"]//p/text()').extract() == []:
            review_p = response.xpath('//div[@class="views-field views-field-body"]//span/text()').extract()
        else:
            review_p = response.xpath('//div[@class="views-field views-field-body"]//p/text()').extract()
        ### replace html spaces
        review = map(lambda s: s.replace("\xa0"," "),review_p)
        ### strip whitespace
        review = list(map(lambda s: s.strip(),review))
        ### join each element in the list with two new lines
        review = "\n\n".join(review)

        item = BeerItem()
        item['name'] = name
        item['image'] = image
        item['brewer'] = brewer
        item['beer_type'] = beer_type
        item['release'] = release
        item['state'] = state
        item['description'] = description
        item['abv'] = abv
        item['ibu'] = ibu
        item['serv_temp'] = serv_temp
        item['hops'] = hops
        item['malts'] = malts
        item['aroma'] = aroma
        item['appearance'] = appearance
        item['flavor'] = flavor
        item['mouthfeel'] = mouthfeel
        item['overall_impression'] = overall_impression
        item['brewer_intro'] = brewer_intro
        item['review'] = review

        yield item










