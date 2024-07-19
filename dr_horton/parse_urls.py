import csv
import re

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

date = current_datetime.strftime('%d/%m/%Y %I:%M:%S %p')


def send_request(url):
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': 'NZTUWQJ3XSSIBQJUKJKEFXZV2UWMPXAPNOXR5KVLNGEEFBJVVUD8ZKHS427T6S68AFNPUZ79BDVRZPVC',
            'url': url,
            'render_js': 'false',
        },

    )
    print('Response HTTP Status Code: ', response.status_code)
    return response.content


def parse_urls(url, ):
    print(url)
    webpage_content = send_request(url)
    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(webpage_content, 'html.parser')

    # Find the <script> tag with type="application/ld+json"
    script_tag = soup.find('script', type='application/ld+json')

    final_dict = {}
    # Extract the JSON content
    if script_tag:
        json_content = script_tag.string.strip()
        print(json_content)
        # Remove the trailing semicolon if it exists
        if json_content.endswith(';'):
            json_content = json_content[:-1]
        try:
            data = json.loads(json_content)
            brand = "Dr Horton"
            final_dict['brand'] = brand

            type_ = data['@type']
            final_dict['type_'] = type_

            url_ = data['url']
            final_dict['url_'] = url_

            try:
                bedrooms = data['numberOfBedrooms']
                final_dict['bedrooms'] = bedrooms
            except Exception as e:
                final_dict['bedrooms'] = ''

            floorsize = data['floorSize']
            final_dict['floorsize'] = floorsize

            try:
                bathroom = data['numberOfBathroomsTotal']
                final_dict['bathroom'] = bathroom
            except Exception as e:
                final_dict['bathroom'] = ''

            latitude = data['latitude']
            final_dict['latitude'] = latitude

            longitude = data['longitude']
            final_dict['longitude'] = longitude

            community = url_.split('/')[6].replace('-', ' ').title()
            final_dict['community'] = community

            market = url_.split('/')[4].title()
            final_dict['market'] = market

            city = data['address']['addresslocality']
            final_dict['city'] = city

            state = data['address']['addressregion']
            final_dict['state'] = state

            fullzips = data['address']['postalcode']
            final_dict['fullzips'] = fullzips

            street_address = data['address']['streetaddress']
            final_dict['street_address'] = street_address

            msa = market
            final_dict['msa'] = msa

        except json.JSONDecodeError as e:
            print("Failed to decode JSON:", e)
    else:
        print("No <script> tag with type='application/ld+json' found.")

    # Find the <script> tag containing the desired JavaScript code
    script_tag_ = soup.find('script', string=re.compile(r'var model ='))

    # Function to find the dictionary containing the value
    def find_dict_containing_value(dict_list, value):
        for dictionary in dict_list:
            if value in dictionary.values():
                return dictionary
        return None

    # Extract the JavaScript content
    if script_tag_:
        script_content = script_tag_.string.strip()

        # Use regex to find the JSON object within the script
        json_match = re.search(r'var model = ({.*?});', script_content, re.DOTALL)
        if json_match:
            json_content = json_match.group(1)
            try:
                data = json.loads(json_content)
                items = data.get('Items', [])
                result_ = find_dict_containing_value(items, final_dict['street_address'])
                if result_:
                    product_num = result_['ItemId']
                    final_dict['product_num'] = product_num

                    price = result_['Price']
                    final_dict['price'] = price

                    garages = result_['NumberOfGarages']
                    final_dict['garages'] = garages

                    stories = result_['NumberOfStories']
                    final_dict['stories'] = stories
                else:
                    final_dict['product_num'] = ''
                    final_dict['price'] = ''
                    final_dict['garages'] = ''
                    final_dict['stories'] = ''

            except json.JSONDecodeError as e:
                print("Failed to decode JSON:", e)
        else:
            print("No JSON object found in the script content.")
    else:
        print("No <script> tag containing the JavaScript found.")
    final_dict['date'] = date

    print("final_dict", final_dict)
    columns = ['brand', 'type_', 'url_', 'bedrooms', 'floorsize', 'bathroom', 'latitude', 'longitude', 'community',
               'market', 'city', 'state', 'fullzips', 'street_address', 'msa', 'product_num', 'price', 'garages',
               'stories', 'date']
    output_file = 'drhorton.csv'
    with open(output_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=columns)
        # writer.writeheader()
        writer.writerows([final_dict])

    print("*" * 30)


if __name__ == '__main__':
    with open('horton_urls_july.txt') as urls:
        result_dict = {}
        urls = [url.strip() for url in urls if 'floor-plans' not in url]

    for url in urls[90:200]:
        if 'floor-plans' not in url:
            parse_urls(url)

