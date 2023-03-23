import scrapy
import json
import requests
from PIL import Image
import os



class AsosscrapSpider(scrapy.Spider):
    name = 'ASOSscrap'
    allowed_domains = ['asos.com']
    start_urls = ['https://www.asos.com/api/product/search/v2/categories/2623?offset=0&store=US&lang=en-US&currency=USD&rowlength=4&channel=desktop-web&country=US&keyStoreDataversion=ornjx7v-36&limit=72&attribute_10992=61379']
    def parse(self, response):
        parse_json = json.loads(response.body)
        data = parse_json['products']
        for item in data :
            image_url = 'https://'+ item['imageUrl'] 
            
            ## store image file ##
            filename = os.path.basename(image_url)
            folder_name = 'asos_images'  # name of the store file
            folder_path = os.path.join(os.getcwd(), folder_name)  # path of the store file
            os.makedirs(folder_path, exist_ok=True)  # create a file if it doesn't exists
            file_path = os.path.join(folder_path, f"{filename}.png")  # complete path of the folder
            with open(file_path, 'wb') as f:
                f.write(requests.get(image_url).content)
            img = Image.open(file_path)
            
            yield{   
            'image_url': image_url
            }
        total_items = parse_json['itemCount']
        pages_number = list(range(0, total_items + 1, 72))
        for pages in pages_number:
            url = f'https://www.asos.com/api/product/search/v2/categories/2623?offset={pages}&store=US&lang=en-US&currency=USD&rowlength=4&channel=desktop-web&country=US&keyStoreDataversion=ornjx7v-36&limit=72&attribute_10992=61379'
            yield scrapy.Request(url=url, callback=self.parse)
        
           
            
        
