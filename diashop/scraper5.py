import requests
import json

def fetch_all_data_from_api(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = json.loads(response.content)
        total_pages = json_data['pagination']['totalPages']
        results = json_data['results']

        for page in range(2, total_pages+1):
            url = api_url.replace(f'&page=1', f'&page={page}')
            response = requests.get(url)
            if response.status_code == 200:
                json_data = json.loads(response.content)
                results += json_data['results']

        return results
    else:
        print('La requête a échoué avec le code:', response.status_code)
        return None




api_url = "https://ylqg8i.a.searchspring.io/api/search/search.json?siteId=ylqg8i&resultsFormat=native&resultsPerPage=28&bgfilter.ss_is_published=1&bgfilter.collection_name=New%20Arrivals&bgfilter.ss_new_45=1&page=1"

results = fetch_all_data_from_api(api_url)

if results is not None:
    data = []
    for item in results:
        res = {
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
        data.append(res)

    with open("data_scraper5/data.json", "w") as f:
        json.dump(data, f)
