# scraper to get data for  every pages with requests

import requests
import json

url = 'https://ylqg8i.a.searchspring.io/api/search/search.json?siteId=ylqg8i&resultsFormat=native&resultsPerPage=28&bgfilter.ss_is_published=1&bgfilter.collection_name=New%20Arrivals&bgfilter.ss_new_45=1&page='

response = requests.get(url + '1')
if response.status_code == 200:
    page_count = 0
    item_count = 0
    json_data = json.loads(response.content)
    total_pages = json_data['pagination']['totalPages']
    data_collection = []
    for page_num in range(1, total_pages+1):
        page_count+=1
        response = requests.get(url + str(page_num))
        #if response.status_code == 200:
        json_data = json.loads(response.content)
        item_data = json_data['results']
        for item in item_data:
            item_count+=1
            results = {
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
            data_collection.append(results)
            print(data_collection)
            print(f"Processed {page_count} pages and collected {item_count} products")
        with open('fullacraper_data/data.json', 'w') as f :
            collection = json.dump(data_collection, f)
        

