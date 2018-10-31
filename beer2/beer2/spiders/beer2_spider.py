from scrapy import Spider, Request
from beer2.items import Beer2Item
import re
import pickle

with open('beer2/beers.pkl', 'rb') as f:
    lst = pickle.load(f)
    f.close()

class Beer2Spider(Spider):
    name = 'beer2_spider'
    allowed_urls = ['https://beerandbrewing.com/']
    start_urls = lst

    def parse(self,response):
        total = response.xpath('//div[@class="main-score-overall rating pure-u-1"]/text()').extract_first()
        aroma_score = response.xpath('//table[@class="table table-hover score-table"]//tr[1]/td[2]/text()').extract_first().strip()
        appearance = response.xpath('//table[@class="table table-hover score-table"]//tr[2]/td[2]/text()').extract_first().strip()
        flavor_score = response.xpath('//table[@class="table table-hover score-table"]//tr[3]/td[2]/text()').extract_first().strip()
        mouthfeel = response.xpath('//table[@class="table table-hover score-table"]//tr[4]/td[2]/text()').extract_first().strip()
        style = response.xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[1]/text()').extract_first()
        if len(response.xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]/text()')) == 2:
            abv = response.xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]/text()').extract()[0].strip()
            ibu = response.xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]/text()').extract()[1].strip()
        else:
            abv = response.xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]/text()').extract()[0].strip()
            ibu = "Not Available"
        paras = response.xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p/text()').extract()
        para = "".join(paras)
        brewer_description = response.xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p[1]/text()').extract_first()[1:-1]
        aroma_description = response.xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p[2]/text()').extract_first().replace('Aroma:','').strip()[1:-1]
        flavor_description = response.xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p[3]/text()').extract_first().replace('Flavor:','').strip()[1:-1]
        overall_description = response.xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p[4]/text()').extract_first().replace('Overall:','').strip()[1:-1]
        image = 'https:' + response.xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/img/@src').extract_first()
        xyz = response.xpath('//div[@class="pure-u-18-24"]/a/@href').extract_first()
        xyz = re.findall('/cbb-beer-review/(\S+)',xyz)[0].replace('-',' ')
        tb = response.xpath('//h1[@style="margin-top:-20px;"]/text()').extract_first()
        brewer = re.findall('(.+) '+xyz,tb,re.IGNORECASE)[0]
        name = re.findall(brewer+' (.+)',tb,re.IGNORECASE)[0]



        item = Beer2Item()
        item['total'] = total
        item['aroma_score'] = aroma_score
        item['appearance'] = appearance
        item['flavor_score'] = flavor_score
        item['mouthfeel'] = mouthfeel
        item['style'] = style
        item['abv'] = abv
        item['ibu'] = ibu
        item['brewer_description'] = brewer_description 
        item['aroma_description'] = aroma_description
        item['flavor_description'] = flavor_description
        item['overall_description'] = overall_description 
        item['image'] = image
        item['brewer'] = brewer
        item['name'] = name

        yield item



        