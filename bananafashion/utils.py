import json
import os


file_path = os.path.join('bananafashion/input_data/womendata.json')
with open(file_path) as f:
    women_new_arrival = json.load(f)
    
    
file_path = os.path.join('bananafashion/input_data/homedata.json')
with open(file_path) as f:
    home = json.load(f)
    
file_path = os.path.join('bananafashion/input_data/workwear.json')
with open(file_path) as f:
    workwear = json.load(f)
#print(women_new_arrival)

# k = data['productCategoryFacetedSearch']['productCategory']['childCategories'][0]['childProducts']
# items = []
# for item in k:
#     items.append(item['businessCatalogItemId'])
# #print(items)

# k2 =  data['productCategoryFacetedSearch']['productCategory']['childCategories'][0]['childProducts']
# items_2  = []
# for item in k2:
#     items_2.append(item['parentStyleId'])
# #print(items_2)