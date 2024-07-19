import json
import requests
from bs4 import BeautifulSoup

with open('urls') as urls:
    urls = [url.strip() for url in urls]

for url in urls:
    print("url is----->>>", url)
    payload = {}

    response = requests.request("GET", url, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all script tags with type 'application/ld+json'
    json_scripts = soup.find_all('script', type='application/ld+json')

    json_list = []
    # Parse and print each JSON data
    for script in json_scripts:
        json_data = json.loads(script.string)
        if 'item' in json_data:
            if len(json_data['item']) == 2:
                if 'lowPrice' in json_data['item'][1]:
                    json_list.append(json_data)

    print(json_list)

    # Save the JSON list to a text file
    with open('json_list_all_locations_v2.txt', 'a') as file:
        for item in json_list:
            file.write(f"{[item]}\n")

    json_list.clear()

