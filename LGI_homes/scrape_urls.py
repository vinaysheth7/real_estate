import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

import random


us_states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New-Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

def generate_unique_number():
    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)
    return random_number


# Get the current date and time
current_datetime = datetime.now()


with open('lgi_home_urls.txt') as urls:
    urls = [url.strip() for url in urls]

for url in urls[583:]:
    print(url)
    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'shell#lang=en; ASP.NET_SessionId=nraorj33repvb2ebqm3qzq3s; sxa_site=BrandSite-Public; SC_ANALYTICS_GLOBAL_COOKIE=e3e57ecc061f418fb859bd56d5186a34|True; _gcl_au=1.1.616895084.1715600447; _ga=GA1.1.115600391.1715600448; lm_ct=true; viewer_token=18f71c15dfa; lm_ssid=v4afhkhhaajehdhjahbbhbfgaaeekabh; _clck=zh170a%7C2%7Cflq%7C0%7C1594; _fbp=fb.1.1715600454955.325777614; invoca_session=%7B%22ttl%22%3A%222024-06-12T11%3A40%3A55.448Z%22%2C%22session%22%3A%7B%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Atrue%7D%7D; __RequestVerificationToken=w2xASOxuhp5pJgsUTX2unoDuUdkIpf9esa7gG-H1V-HVpEyU8Ym9WoATCppOCWCt0VFW8lszl94TGyqk912l3eNOO17ucnHKyVdc1ybFoDw1; lgi_resume_journey_floorplan={73534333-4c92-4e53-adf0-aa3486b8f449}; session_pages=5; lgi_resume_journey_community={cd9336fd-afd2-49f6-a1f7-18d94418d488}; _ga_0K4FHKH8XV=GS1.1.1715600447.1.1.1715602176.39.0.849063102; _uetsid=a4483ab0111d11efbf6d4f589a2e8f91; _uetvid=a4484ef0111d11efb05bc74a21446f25; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNjAzMTQ4YmItYjRjMC00ZTU4LWIxYjctNGZkYTI4MjUzMjk4JTIyJTJDJTIyZSUyMiUzQTE3MTYxMjc3Nzc2ODYlN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyYWRkNmUxNzktNzk2Ni00YzAwLTljYTAtNWMyZGFlNzYzYmVlJTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTcxNTYwMzk3ODIyNiU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNjFkMjFkNjktYjhjOS00Zjk0LTg1ZmQtN2ZiMmJmYjZmOWY4JTIyJTJDJTIyZSUyMiUzQTE3MTYxMjc3Nzc2ODclN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMTYlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNzE1NjAzOTc4MjI2JTdEJTJDJTIyTUdYX0VJRCUyMiUzQSU3QiUyMnYlMjIlM0ElMjJuc19zZWdfMDAwJTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTcxNTYwMzk3ODIyNiU3RCU3RA==; _clsk=1owutgx%7C1715602179201%7C17%7C1%7Cw.clarity.ms%2Fcollect; sxa_site=BrandSite-Public',
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

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all script tags with type 'application/ld+json'
    json_script = soup.find('script', type='application/ld+json')

    json_data = json.loads(json_script.string)
    print(json_data)
    result_dict = {}

    try:
        print("inside try")
        price_text = json_data['@graph'][1]['priceRange'].split('-')[0]
        result_dict['brand'] = 'LGI'
        result_dict['url'] = url
        result_dict['price'] = price_text
        result_dict['date'] = current_datetime.strftime('%d/%m/%Y %I:%M:%S %p')

        product_num = generate_unique_number()
        result_dict['product_num'] = product_num

        result_dict['community'] = json_data['@graph'][1]['contactPoint']['email'].split('@')[0]
        result_dict['market'] = url.split('/')[4]
        result_dict['city'] = json_data['@graph'][1]['address']['addressLocality']

        result_dict['state'] = json_data['@graph'][1]['address']['addressRegion']
        result_dict['fullzips'] = json_data['@graph'][1]['address']['postalCode']
        result_dict['msa'] = url.split('/')[4].title()
        result_dict['collection'] = ''

    except Exception as e:
        try:
            price_text = soup.find('li', class_='price-item').get_text(strip=True).replace('/mo†', '').replace(',',
                                                                                                               '').replace(
                '$', '')
        except Exception as e:
            price_text = ''

        print("inside exception")
        result_dict['brand'] = 'LGI'
        result_dict['url'] = url
        result_dict['price'] = price_text
        result_dict['date'] = current_datetime.strftime('%d/%m/%Y %I:%M:%S %p')

        product_num = generate_unique_number()
        result_dict['product_num'] = product_num

        result_dict['community'] = url.split('/')[-1]
        result_dict['market'] = url.split('/')[4]
        result_dict['city'] = json_data['@graph'][0]['itemListElement'][1]['item']['name']

        result_dict['state'] = us_states[url.split('/')[3].title().replace('-',' ')]
        result_dict['fullzips'] = soup.find('span', class_='zip').get_text(strip=True)
        result_dict['msa'] = url.split('/')[4].title()
        result_dict['collection'] = ''
    print("result_dict-->>", result_dict)

    # Specify your output file name
    output_file = 'lgi_home.csv'
    with open(output_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=['product_num', 'brand', 'url', 'community', 'market',
                                            'state', 'collection', 'city', 'fullzips', 'msa', 'price', 'date'])
        # writer.writeheader()
        writer.writerows([result_dict])
    print(result_dict)
