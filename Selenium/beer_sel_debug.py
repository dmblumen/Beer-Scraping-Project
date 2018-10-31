from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import re
import csv

lst = ["https://beerandbrewing.com/review/time-crystals-1/","https://beerandbrewing.com/review/justice-temple/","https://beerandbrewing.com/review/the-original-006/","https://beerandbrewing.com/review/crookedstaveipa/","https://beerandbrewing.com/review/space-traveler/","https://beerandbrewing.com/review/top-cutter/"]
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
            ll = ll.replace('Aroma: ','')
            ll = ll.replace('Flavor: ','')
            ll = ll.replace('Overall: ','')
            ll = "".join(ll)
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
    index += 1
    print("Finished page",index)

driver2.close()