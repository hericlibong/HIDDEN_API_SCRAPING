
# code for get only datas of the first page
import requests
import json

url =  'https://ylqg8i.a.searchspring.io/api/search/search.json?siteId=ylqg8i&resultsFormat=native&resultsPerPage=28&bgfilter.ss_is_published=1&bgfilter.collection_name=New%20Arrivals&bgfilter.ss_new_45=1&page=1'


response = requests.get(url)

if response.status_code == 200:
    json_data = json.loads(response.content)
    item_data = json_data['results']
    for item in  item_data:
        brand = item['brand']
        name = item['name']
        ss_name = item['ss_name']
        price =  item['price']
        variant_price = ['variant_compare_at_price']
        msrp = item['msrp']
        product_type = item['product_type_unigram']
        stock = item['ss_instock_pct']
        sku = item['sku']
        color_scheme = item['tags_dia_color_scheme']
        primary_color = item['tags_dia_primary_color']
        description = item['body_html']
        images = item['images']
        results = {
            'Collection': 'New Arrival',
            'Brand':brand,
            'Name':name,
            'ssName':ss_name,
            'Price':price,
            'variantComparePrice':variant_price,
            'msrp':msrp,
            'ProductType':product_type,
            'Stock':stock,
            'sku':sku,
            'colorScheme': color_scheme,
            'primaryColor': primary_color,
            'Description':description,
            'Images':images
            
        }
        print(results)
        
  