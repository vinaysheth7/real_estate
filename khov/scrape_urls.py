import csv
import json
import re

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random


def generate_unique_number():
    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)
    return random_number


# Get the current date and time
current_datetime = datetime.now()

with open('khov_urls_12june.txt') as urls:
    result_dict = {}
    urls = [url.strip() for url in urls]

# urls = ["https://www.khov.com/find-new-homes/california/indio/92203/k-hovnanian-homes/aguila-at-terra-lago",
#         "https://www.khov.com/find-new-homes/delaware/millville/19967/k-hovnanian-homes/egret-shores/barcelona",
#         "https://www.khov.com/find-new-homes/texas/van-alstyne/556-brook-view-drive-homesite-f-31/75495/k-hovnanian-homes/rolling-ridge/sweet-pea---556-brook-view-f-31"]

for url in urls[655:]:
    print(url)
    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'brand=%22KHV%22; ai_user=N4N1h|2024-04-30T10:46:32.827Z; googleRef=null; atlasvid=%7B%22visitorid%22%3A%2289723cc9-3ca7-41ea-a563-a4f0d73766f6%22%7D; atlasseg_3d5525157d8545a0b9e2d8d8295374aa=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.khov.com%2Ffind-new-homes%22%2C%22state%22%3A%22DE%22%2C%22division%22%3A%22Felton%22%2C%22community%22%3Anull%2C%22plan%22%3Anull%2C%22source%22%3Anull%2C%22medium%22%3Anull%2C%22campaign%22%3Anull%2C%22campaignContent%22%3Anull%7D; _gid=GA1.2.1424854594.1715247483; _gcl_au=1.1.66621899.1715247484; _hjSessionUser_801259=eyJpZCI6Ijc5NmE1ODRjLTMxNDMtNTVhMy04OGNjLTQ5NjM3MzE4NTliNyIsImNyZWF0ZWQiOjE3MTUyNDc0ODQ0NzEsImV4aXN0aW5nIjp0cnVlfQ==; Geolocation=%22JH%22; _fbp=fb.1.1715247500022.1464512683; _pin_unauth=dWlkPVlqRXdPREF5TURJdE1EUXpaaTAwTlRabExXSXpabUl0WlRWbVlUY3paRFV4T1Rrdw; privacypolicyagree=yes; lastVisitedState=%7B%22stateName%22%3A%22arizona%22%7D; userstate=%22JH%22; requestInfoInterstitial=%22tabbed%22; _hjSession_801259=eyJpZCI6IjA4Y2E3ZmMzLTdiMjUtNDRjNi1hYjMzLTIxYTU1NmNhNTViMiIsImMiOjE3MTUyNTM3ODUyNjcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; recent=%5B%7B%22groupName%22%3A%22Buckeye%2C%20Arizona%22%2C%22name%22%3A%22K.%20Hovnanian\'s%C2%AE%20Four%20Seasons%20at%20Victory%20at%20Verrado%22%2C%22url%22%3A%22%2Ffind-new-homes%2Farizona%2Fbuckeye%2F85396%2Ffour-seasons%2Fk.-hovnanian%26%2339%3Bs-four-seasons-at-victory-at-verrado%22%2C%22image%22%3A%22%2Fazure%2Fsitefinitylibraries%2Fimages%2Fdefault-source%2Fimages%2Faz%2Ffour-seasons-victory-at-verrado%2Faspots%2Fvictory-at-verrado-golf.jpg%3Fsfvrsn%3Dfc20b69b_4%26amp%3Bbuild%3D6111%26amp%3Bencoder%3Dwic%26amp%3Buseresizingpipeline%3Dtrue%22%2C%22stateUrlName%22%3A%22arizona%22%7D%2C%7B%22groupName%22%3A%22League%20City%2C%20Texas%22%2C%22name%22%3A%22Westwood%22%2C%22url%22%3A%22%2Ffind-new-homes%2Ftexas%2Fleague-city%2F77573%2Fk-hovnanian-homes%2Fwestwood%22%2C%22image%22%3A%22%2Fazure%2Fsitefinitylibraries%2Fimages%2Fdefault-source%2Fimages%2Fcorp%2Fspring-campaign-2024%2Fhou%2Feast-houston---a-spot_4-30.jpeg%3Fsfvrsn%3Db5aa0885_0%26amp%3Bbuild%3D6111%26amp%3Bencoder%3Dwic%26amp%3Buseresizingpipeline%3Dtrue%22%2C%22stateUrlName%22%3A%22texas%22%7D%5D; _gat=1; ai_session=8o+zQ|1715253337597|1715253890311.1; _uetsid=dd2d58900de711ef90236316ec4b79c6; _uetvid=dd2d6aa00de711ef99b1b5882dab678f; _ga_HQ8C1WMK7C=GS1.1.1715253784.2.1.1715253905.40.0.0; _ga=GA1.2.180673466.1714473978; _gat_AtlasRTXTracker=1; sessionId=006a0405-0b38-4ef9-b7a3-c4cf2812145e; sessionId=0ab1b78a-a8b8-4614-97cb-4a8dac454326',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

        # print(response.content)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <iframe> element with the specified id
        iframe_element = soup.find('iframe', id='interactive-site-plan')

        # Check if the element is found and extract the data-src attribute
        if iframe_element:
            data_src = iframe_element.get('data-src')
            result_dict['data_src'] = data_src
            print(f'data-src: {data_src}')
        else:
            result_dict['data_src'] = 'No Plan'
            print('Element with id "interactive-site-plan" not found.')

        # Find all <p> elements
        p_elements = soup.find_all('p')

        # Define a regex pattern to extract the number
        pattern = re.compile(r'Approx\. Sq Ft: ([\d,]+)')

        # Iterate over the <p> elements and extract the square footage
        for p in p_elements:
            match = pattern.search(p.text)
            if match:
                sq_ft = match.group(1)
                result_dict['sq_ft'] = sq_ft
                break
            else:
                result_dict['sq_ft'] = ''

        # Extract the JSON data from the 'data-content' attribute
        data_content = soup.find('button', class_='tooltip__calc')['data-content']

        # Decode the HTML entities in the JSON data
        decoded_data_content = BeautifulSoup(data_content, 'html.parser').text

        # Load the JSON data
        price_json_data = json.loads(decoded_data_content)


        # Now you can access the JSON data as a Python dictionary
        print(price_json_data, '\n')

        brand = "Hovnanian"
        url = url
        price = price_json_data['basePrice']
        date = current_datetime.strftime('%d/%m/%Y %I:%M:%S %p')

        result_dict['brand'] = brand
        result_dict['url'] = url
        result_dict['price'] = price
        result_dict['date'] = date

        product_num = generate_unique_number()
        result_dict['product_num'] = product_num
        result_dict['title'] = ''

        # Find the <script> tag with type 'application/ld+json'
        script_tag = soup.find('script', type='application/ld+json')

        latitude= ''
        longitude = ''

        if script_tag:
            # Extract the JSON data from the text of the <script> tag
            adddress_json_data = json.loads(script_tag.text)
            latitude = adddress_json_data['geo']['latitude']
            longitude = adddress_json_data['geo']['longitude']
            community = adddress_json_data['brand']
            market = adddress_json_data['address']['addressLocality'].title()
            state = adddress_json_data['address']['addressRegion']
            fullzips = adddress_json_data['address']['postalCode']
            msa = market
            collection = adddress_json_data['name']
            type = adddress_json_data['mainEntityOfPage']['specialty']

            result_dict['community'] = community
            result_dict['market'] = market
            result_dict['state'] = state
            result_dict['fullzips'] = fullzips
            result_dict['msa'] = msa
            result_dict['collection'] = collection
            result_dict['type'] = type
            result_dict['latitude'] = latitude
            result_dict['longitude'] = longitude
        else:
            url_parts = url.split('/')
            market = url_parts[4]
            state = url_parts[5]
            fullzips = url_parts[6]
            msa = market
            community = url_parts[7].replace('-', ' ').title()
            collection = url_parts[-1]

            result_dict['brand'] = 'Hovnanian'
            result_dict['community'] = community
            result_dict['market'] = market
            result_dict['state'] = state
            result_dict['fullzips'] = fullzips
            result_dict['msa'] = msa
            result_dict['collection'] = collection
            result_dict['type'] = ''
            result_dict['latitude'] = latitude
            result_dict['longitude'] = longitude

        # Specify your output file name
        output_file = 'khov_homes_12june.csv'
        with open(output_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile,
                                    fieldnames=['product_num', 'brand', 'url', 'type', 'title', 'community', 'market',
                                                'state', 'collection', 'city', 'fullzips', 'msa', 'latitude', 'longitude', 'price', 'sq_ft', 'data_src', 'date'])
            # writer.writeheader()
            writer.writerows([result_dict])
        print(result_dict)

    except requests.exceptions.Timeout:
        print("The request timed out")
    except requests.exceptions.RequestException as e:
        # Handle other request exceptions (e.g., network errors, invalid URLs, etc.)
        print(f"An error occurred: {e}")

    except Exception as e:
        print(e, "-------->>>", url)
