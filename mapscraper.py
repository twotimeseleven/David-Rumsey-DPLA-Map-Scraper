#!/usr/bin/python3
import requests
import wget
import urllib.request
import psutil
import re
import time
import os

def getPhotos():
        x = 0
        api_key = os.environ['DPLA_API_KEY']
        for page in range(1, 101):
                req = 'https://api.dp.la/v2/items?sourceResource.collection.title=*Rumsey*&page_size=500&api_key=' + str(api_key) + '&object&page=' + str(page)
                r = requests.get(req).json()
                for item in r['docs']:
                        if 'Rumsey' in item['dataProvider'] and "image" in item['sourceResource']['type'] and x > 47:
                                link = requests.get(str(item['isReferencedBy'])).json()
                                name = "/home/faroe/DPLA/Maps/" + str(x) + '.jp2'
                                datalist = link['sequences'][0]['canvases'][0]['metadata']

                                for data in datalist:
                                        if 'Download 1' in data['label']:
                                                download = re.findall('href=(.*\.jp2)', data['value'])
                                                if not download:
                                                        print('Invalid download for file: ' + str(data['label']))
                                                break
                                if download:
                                        download = download[0]
                                        if download[-4:] == '.jp2':
                                                print('Downloading file: ' + str(download))
                                                f = open(name,'wb+')
                                                f.write(urllib.request.urlopen(download).read())
                                                f.close()
                                time.sleep(5)
                        x += 1
getPhotos()
