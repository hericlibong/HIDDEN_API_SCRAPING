import os
import json
import pandas as pd
import csv
from utils import women_new_arrival, home, workwear

# How to scrap data without any python scraping librairies throught  hidden API

# construire le chemin de fichier avec os.path.join
# file_path = os.path.join('womendata.json')

# # ouvrir le fichier avec le chemin construit
# with open(file_path) as f:
#     data = json.load(f)
    
collections = workwear['productCategoryFacetedSearch']['productCategory']['childCategories']
categorie = workwear['productCategoryFacetedSearch']['productCategory']['name']

data_collection = []
for collection in collections:
    Collection = collection['name']
    collection_item = collection['childProducts']
    for item in collection_item:
        item_id = item['businessCatalogItemId']
        item_name = item['name']
        item_date = item['inDcDate']
        product_stock = item['isInStock']
        try : 
            pristine_image = 'https://bananarepublic.gap.comproduct' + item.get('pristineImages', {}).get('pristine1ImagePath')
        except Exception as e:
            pristine_image = None
        zoom_image  = 'https://bananarepublic.gap.com' + item['zoomImages']['p01ZoomImagePath']
        quick_image = item['quicklookImage']['path']
        large_image = 'https://bananarepublic.gap.com' + item['categoryLargeImage']['path']
        sailor = item.get('vendor', {}).get('webVendorName')
        current_maxprice = item['price']['currentMaxPrice']
        current_minprice  = item['price']['currentMinPrice']
        regular_maxprice  = item['price']['regularMaxPrice']
        regular_minprice  = item['price']['regularMinPrice']
        product_type  = item['webProductType']
    
    
    
        results = {
            'categorie':categorie,
            'Collection':Collection,
            'itemID':item_id,
            'name': item_name,
            'date' : item_date,
            'stock' :product_stock,
            'pristinePicture': pristine_image,
            'imageZoom': zoom_image,
            'imageQuick': quick_image,
            'imageLarge':large_image,
            'vendeur' : sailor,
            'currentMaxprice':current_maxprice, 
            'currentMinprice': current_minprice,
            'regularMaxprice':regular_maxprice,
            'ragularMinprice':regular_minprice,
            'productType':product_type 
            
                       
        }
        data_collection.append(results)
        with open('bananafashion/output_data/WorkWear.json',  'w') as f :
            collection=json.dump(data_collection, f, indent=3)
        
            print(data_collection)
# df = pd.json_normalize(data_collection)
# df.to_csv('data.csv')
