import scrapy
import json


class DiashopspiderSpider(scrapy.Spider):
    name = 'diashopspider'
   
    allowed_domains = ['ylqg8i.a.searchspring.io']
    start_urls = ['https://ylqg8i.a.searchspring.io/api/search/search.json?siteId=ylqg8i&resultsFormat=native&resultsPerPage=28&bgfilter.ss_is_published=1&bgfilter.collection_name=New%20Arrivals&bgfilter.ss_new_45=1&page=1']
 
    def parse(self, response):
        parse_json = json.loads(response.body)
        items = parse_json['results'] 
        for item in items:
            yield {
            "Collection": "New Arrival",
            "Brand": item["brand"],
            "Name": item["name"],
            "ssName": item["ss_name"],
            "Price": item["price"],
            "VariantComparePrice": item.get("variant_compare_price", "None"),
            "Msrp": item["msrp"],
            "ProductType": item["product_type_unigram"],
            "Stock": item["ss_instock_pct"],
            "Sku": item["sku"],
            "colorScheme": item.get("tags_dia_color_scheme", "None"),
            "PrimaryColor": item.get("tags_dia_primary_color", "None"),
            "Description": item.get("body_html", "None"),
            "Images": item.get("images", "None"),
                
            }
        current_page = parse_json['pagination']['currentPage']
        next_page_check = parse_json['pagination']['nextPage']
        if next_page_check!=0: 
            next_page = current_page + 1
            next_page_url = f'https://ylqg8i.a.searchspring.io/api/search/search.json?siteId=ylqg8i&resultsFormat=native&resultsPerPage=28&bgfilter.ss_is_published=1&bgfilter.collection_name=New%20Arrivals&bgfilter.ss_new_45=1&page={next_page}'
            yield scrapy.Request(url=next_page_url, callback=self.parse)
       
        
        
            
        
        
        
        
        
       
            
