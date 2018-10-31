from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import re
import csv

with open('beers.pkl', 'rb') as f:
    lst = pickle.load(f)
    f.close()

#driver = webdriver.Chrome()
#result_urls = ['https://beerandbrewing.com/beer-reviews/?q=&hPP=20&idx=cbb_web_review_search&p={}'.format(x) for x in range(50)]
#lst = []
#for url in result_urls:
#    driver.get(url)
#    for i in range(1,21):
#        link = driver.find_element_by_xpath('//*[@id="hits"]/div/div[{}]/div/div/a'.format(i)).get_attribute('href')
#        print(link)
#        print("=" * 50)
#        lst.append(link)
#    print("Finished Page",url)
#driver.close()

csv_file = open('reviews2.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)
review_dict = {}
driver2 = webdriver.Chrome()
index = 0
for url in lst:
    driver2.get(url)
    try:
        title = driver2.find_element_by_xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/h1').text
        print("title",title)
        print("=" * 50)
    except Exception as e:
        print(e)
        title = "Fail!"
    try:
        total = driver2.find_element_by_xpath('//div[@class="main-score-overall rating pure-u-1"]').text
        total = re.findall('(.+)/100',total)[0]
        print("total",total)
        print("=" * 50)
    except Exception as e:
        print(e)
        total = "Fail!"
    try:
        aroma_score = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-10-24"]//tr[1]/td[2]').text
        print("aroma_score",aroma_score)
        print("=" * 50)
    except Exception as e:
        print(e)
        aroma_score = "Fail!"
    try:
        appearance = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-10-24"]//tr[2]/td[2]').text
        print("appearance",appearance)
        print("=" * 50)
    except Exception as e:
        print(e)
        appearance = "Fail!"
    try:
        flavor_score = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-10-24"]//tr[3]/td[2]').text
        print("flavor_score",flavor_score)
        print("=" * 50)
    except Exception as e:
        print(e)
        flavor_score = "Fail!"
    try:
        mouthfeel = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-10-24"]//tr[4]/td[2]').text
        print("mouthfeel",mouthfeel)
        print("=" * 50)
    except Exception as e:
        print(e)
        mouthfeel = "Fail!"
    try:
        image = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/img').get_attribute('src')
        print("image",image)
        print("=" * 50)
    except Exception as e:
        print(e)
        image = "Fail!"
    try:
        style = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[1]').text
        style = style.replace('Style: ','')
        print("style",style)
        print("=" * 50)
    except Exception as e:
        print(e)
        style = "Fail!"
    try:
        try:
            abv = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]').text
            if len(abv) > 0:
                abv = re.findall('ABV: (.+\..+) IBU:',abv)[0]
                print("abv",abv)
                print("=" * 50)
            else:
                abv = "Not Available"
                print("abv",abv)
                print("=" * 50)
        except Exception as e:
            print(e)
            abv = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]').text
            if len(abv) > 0:
                abv = re.findall('ABV: (.+\..+)',abv)[0]
                print("abv",abv)
                print("=" * 50)
            else:
                abv = "Not Available"
                print("abv",abv)
                print("=" * 50)
    except:
        abv = "Not Available"
        print("abv",abv)
        print("=" * 50)
    try:
        ibu = driver2.find_element_by_xpath('//div[@class="pure-u-1 pure-u-md-7-24"]/p[2]').text
        ibu = re.findall('IBU: (.+)',ibu)[0]
        print("ibu",ibu)
        print("=" * 50)
    except Exception as e:
        ibu = "Not Available"
        print("ibu",ibu)
        print("=" * 50)
    try:
        ll = []
        paras = driver2.find_elements_by_xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p')
        for element in paras:
            ll.append(element.text)
        ll = "".join(ll)
        ll = ll.replace('Aroma: ','')
        ll = ll.replace('Flavor: ','')
        ll = ll.replace('Overall: ','')
        ll = re.split('”“',ll)
        print(len(ll))
        if len(ll) > 3:
            ll = []
            paras = driver2.find_elements_by_xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p')
            for element in paras:
                ll.append(element.text)
            ll = "".join(ll)
            ll = ll.replace('Aroma: ','')
            ll = ll.replace('Flavor: ','')
            ll = ll.replace('Overall: ','')
            ll = re.split('”“',ll)
            brewer_description = ll[0][1:]
            print("brewer_description",brewer_description)
            print("=" * 50)
            aroma_description = ll[1]
            print("aroma_description",aroma_description)
            print("=" * 50)
            flavor_description = ll[2]
            print("flavor_description",flavor_description)
            print("=" * 50)
            overall_description = ll[3][:-1]
            print("overall_description",overall_description)
            print("=" * 50)
        elif len(ll) == 2:
            ll = []
            paras = driver2.find_elements_by_xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p')
            for element in paras:
                ll.append(element.text)
            ll = "".join(ll)
            ll = re.split('”“',ll)
            brewer_description = ll[0][1:]
            print("brewer_description",brewer_description)
            print("=" * 50)
            overall_description = ll[1][:-1]
            print("overall_description",overall_description)
            print("=" * 50)
            flavor_description = "Not Available"
            aroma_description = "Not Available"
        else:
            ll = []
            paras = driver2.find_elements_by_xpath('//div[@class="text-wrapper pure-u-1 pure-u-md-1"]/p')
            for element in paras:
                ll.append(element.text)
            ll = "".join(ll)
            brewer_description = re.findall('(.+)Aroma',ll)[0].strip().replace('“','')
            brewer_description = brewer_description.replace('”','')
            brewer_description = brewer_description.replace('"','')
            print("brewer_description",brewer_description)
            aroma_description = re.findall('Aroma:(.+)Flavor',ll)[0].strip().replace('“','')
            aroma_description = aroma_description.replace('”','')
            aroma_description = aroma_description.replace('"','')
            print("aroma_description",aroma_description)
            flavor_description = re.findall('Flavor:(.+)Overall',ll)[0].strip().replace('“','')
            flavor_description = flavor_description.replace('”','')
            flavor_description = flavor_description.replace('"','')
            print("flavor_description",flavor_description)
            overall_description = re.findall('Overall:(.+)',ll)[0].strip().replace('“','')
            overall_description = overall_description.replace('”','')
            overall_description = overall_description.replace('"','')
            print("overall_description",overall_description)
    except Exception as e:
        print(e)
        overall_description = "Fail"
        brewer_description = "Fail"
        aroma_description = "Fail"
        flavor_description = "Fail"
    try:
        tbsplit = driver2.find_element_by_xpath('//div[@class="pure-u-18-24"]/a').get_attribute('href')
        print(tbsplit)
        xyz = re.findall('/cbb-beer-review/(\S+)',tbsplit)[0].replace('-',' ')
        print(re.findall(' ',xyz))
        if len(re.findall(' ',xyz)) > 0:
            xyz = xyz.split(' ')
            print(xyz[0][:-2])
            brewer = re.findall('(.+) '+xyz[0][:-2],title,re.IGNORECASE)[0]
            print("brewer",brewer)
            print("=" * 50)
            name = re.findall(brewer+' (.+)',title,re.IGNORECASE)[0]
            print("name",name)
            print("=" * 50)
        elif len(re.findall('(.+) '+xyz[0][:-2],title,re.IGNORECASE)) > 0:
            brewer = re.findall('(.+) '+xyz[0][:-2],title,re.IGNORECASE)[0]
            print("brewer",brewer)
            print("=" * 50)
            name = re.findall(brewer+' (.+)',title,re.IGNORECASE)[0]
            print("name",name)
            print("=" * 50)
        else:
            name = title
            brewer = "Fail, See Title"
    except Exception as e:
        print(e)
        name = "Fail"
        brewer = "Fail"


    review_dict["link"] = url
    review_dict["title"] = title
    review_dict["image"] = image
    review_dict["total"] = total
    review_dict["style"] = style
    review_dict["abv"] = abv
    review_dict["ibu"] = ibu
    review_dict["aroma_score"] = aroma_score
    review_dict["appearance"] = appearance
    review_dict["flavor_score"] = flavor_score
    review_dict["mouthfeel"] = mouthfeel
    review_dict["brewer_description"] = brewer_description
    review_dict["aroma_description"] = aroma_description
    review_dict["flavor_description"] = flavor_description
    review_dict["overall_description"] = overall_description
    review_dict["tbsplit"] = tbsplit
    review_dict["name"] = name
    review_dict["brewer"] = brewer

    writer.writerow(review_dict.values())
    index += 1
    print("Finished with Page",index)
csv_file.close()
driver2.close()
        

        

