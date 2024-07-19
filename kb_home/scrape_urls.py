import csv
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

with open('kb_home_urls.txt') as urls:
    result_dict = {}
    urls = [url.strip() for url in urls]

for url in urls:

    print(url)
    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'EPiStateMarker=true; ARRAffinity=4ab65a0346cca8a3aa76d4918984fb5bba5a7ce0188d2e173bcc9dbcb1d36bd2; ARRAffinitySameSite=4ab65a0346cca8a3aa76d4918984fb5bba5a7ce0188d2e173bcc9dbcb1d36bd2; ai_user=NnFn0j/t0ysCfm6E4wFLnl|2024-04-30T10:48:20.291Z; atlasvid=%7B%22visitorid%22%3A%2260e7ccc8-77ad-449d-b15d-bfac0410ac33%22%7D; msd365mkttr=dyt5eg76XxXeUvqOhQIrea6glQ73TXZCksTEYP8X; msd365mkttrs=UOiHbsAt; kbh.recent.region=14; .AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8IUWs55mejhPpKk6ZBC8-LvSwXjzoYuXODdP7L_K-A38sRpYePIegHEftTxC7Tn82Lg_sCwEF4mRysWW6VUWaKceOr7ShDuHkXEA5eOBvPJHGRmCwis8Z2OhNb2rmdYZmk4POPCSgJA5VzVVQFZq6Kw; atlasseg_575bd48a7531400885414037bfb89219=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.kbhome.com%2F%22%2C%22srcUrl%22%3A%22https%3A%2F%2Fwww.kbhome.com%2Fnew-homes-phoenix%22%2C%22division%22%3A%22Phoenix%22%2C%22community%22%3Anull%2C%22plan%22%3Anull%2C%22source%22%3Anull%2C%22medium%22%3Anull%2C%22campaign%22%3Anull%7D; _vwo_uuid_v2=D91E3030D7F14288A22127B066E4A819C|4bc119db5c83116c4d70b836d446f2fd; _hjSessionUser_139514=eyJpZCI6ImUwMDhkOGVhLTQ1NjEtNTMxMi1iNzU4LWUzOWUzZTBhZjQ3MiIsImNyZWF0ZWQiOjE3MTUzMzQzNzI4ODUsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.583398162.1715334374; _fbp=fb.1.1715334374147.756274761; _pin_unauth=dWlkPVlqRXdPREF5TURJdE1EUXpaaTAwTlRabExXSXpabUl0WlRWbVlUY3paRFV4T1Rrdw; _gid=GA1.2.800245453.1715334377; ai_session=jeME2iPx1YzZwl3qfxCop0|1715350923573|1715350923573; _ga_KG7636GCER=GS1.1.1715350924.2.0.1715350924.60.0.0; utag_main=v_id:018f2e9ea80c001e479e924194cd05075001706d00942$_sn:3$_se:1$_ss:1$_st:1715352724023$dc_visit:3$ses_id:1715350924023%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$pre_page:%2Fnew-homes-phoenix%2Farroyo-vista-ii%2Fplan-1330%3Bexp-session$dc_region:us-west-2%3Bexp-session; _hjSession_139514=eyJpZCI6IjNlY2NiNmI2LTYwMzQtNGI1ZC1hNTFkLTU5MDQ1ODdjNzZiOCIsImMiOjE3MTUzNTA5MjUyOTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _ga=GA1.2.1350967677.1715334374; _bts=52373811-f208-4ca6-de4b-9dabc714f2d9; _bti=%7B%22app_id%22%3A%22kb-home%22%2C%22bsin%22%3A%22ucvJWdQZPzSXRC4MjqwMj8E3NhemVnQzBia4zXX7IUVT85z48OWDIaQ4%2B8Z%2FEoG1AkZdTm%2FZxin70IfVD%2B2uOQ%3D%3D%22%2C%22is_identified%22%3Afalse%7D; _gat_AtlasRTXTracker=1',
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

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <a> tags with class "text-link cta-directions"
    target_a_tags = soup.find_all('a', class_='text-link cta-directions')

    address = ""
    # Extract information from each <a> tag
    for tag in target_a_tags:
        text = tag.get_text(strip=True)
        href = tag['href']
        address = text

    print(address)

    # # Define a regular expression pattern to match the house number
    # pattern = r'\b\d+\b'  # Matches one or more digits surrounded by word boundaries
    #
    # # Use re.findall to find all matches of the pattern in the address string
    # house_numbers = re.findall(pattern, address)
    #
    # # If house_numbers is not empty, get the first item (assuming there's only one house number)
    # if house_numbers:
    #     fullzips = house_numbers[0]
    #     print("fullzips", fullzips)
    # else:
    #     fullzips = ''

    # Find all <script> tags in the HTML
    script_tags = soup.find_all('script')

    # Loop through each <script> tag and extract data if it matches certain criteria
    for script_tag in script_tags:
        date = current_datetime.strftime('%d/%m/%Y %I:%M:%S %p')

        result_dict = {}
        script_content = script_tag.text
        if "dataLayer.page['divison']" in script_content:
            # Parse the data from the <script> tag as shown in the previous example
            price_data = {}
            lines = script_content.split('\n')
            for line in lines:
                if '=' in line:
                    key, value = line.split('=')
                    key = key.split("dataLayer.page['")[-1].replace("'] ", "").strip()
                    value = value.strip().strip("';")
                    price_data[key] = value

            print(price_data)

            result_dict['brand'] = 'KB Home'
            result_dict['url'] = url
            result_dict['price'] = price_data['plan price']
            result_dict['date'] = date

            product_num = generate_unique_number()
            result_dict['product_num'] = product_num

            result_dict['community'] = price_data['community name']
            result_dict['market'] = price_data['region name']
            result_dict['city'] = price_data['region name']

            result_dict['state'] = price_data['state']
            result_dict['fullzips'] = address.split(price_data['state'])[-1]
            result_dict['msa'] = price_data['region name']
            result_dict['collection'] = ''

            # Specify your output file name
            output_file = 'kb_home.csv'
            with open(output_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile,
                                        fieldnames=['product_num', 'brand', 'url', 'community', 'market',
                                                    'state', 'collection', 'city', 'fullzips', 'msa', 'price', 'date'])
                # writer.writeheader()
                writer.writerows([result_dict])
            print(result_dict)
