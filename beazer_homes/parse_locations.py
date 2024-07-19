import csv
import json
import random
from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()

date = current_datetime.strftime('%d/%m/%Y %I:%M:%S %p')


def generate_unique_number():
    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)
    return random_number

market_mapping = {"atlanta-ga": "Atlanta", "charleston-sc": "Charleston", "dallas-tx": "Dalas",
                  "delaware-beaches-de": "Delaware", "houston-tx": "Houston", "indianapolis-in": "Indianapolis",
                  "las-vegas-nv": "Las Vegas", "maryland--dc-md": "Maryland / D.C.", "myrtle-beach-sc": "Myrtle Beach",
                  "nashville-tn": "Nashville", "orlando-fl": "Orlando", "phoenix-az": "Phoenix", "raleigh-durham-nc": "Raleigh Durham",
                  "sacramento-ca": "Sacramento", "san-antonio-tx": "San Antonio", "southern-california-ca": "South California",
                  "virginia--dc-va": "Virginia / D.C."}


# Open the text file in read mode
with open('json_list_all_locations.txt', 'r') as file:
    # Read the contents of the file
    data = file.read()

# Replace single quotes with double quotes
data_fixed = data.replace("'", '"')

# Split the data into individual dictionary strings based on the newline character
dict_list = data_fixed.split('\n')

# Parse each dictionary string into a Python dictionary object
parsed_dicts = []
for dict_str in dict_list:
    try:
        parsed_dict = json.loads(dict_str)
        parsed_dicts.append(parsed_dict)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

# Now you can work with the parsed dictionaries as needed
for parsed_dict in parsed_dicts:
    final_result = {}
    data = parsed_dict[0]

    brand = "Beazer Homes"
    final_result['brand'] = brand

    url = data['item'][0]['url']
    final_result['url'] = url

    product_num = generate_unique_number()
    final_result['product_num'] = product_num

    type = data['item'][0]['@type']
    final_result['type'] = type

    community = data['item'][0]['name']
    final_result['title'] = community
    final_result['community'] = url.split(url.split('/')[3])[-1].split('/')[1].title().replace('-', ' ').strip()

    market = url.split('/')[3]
    final_result['market'] = market_mapping[market]

    state = data['item'][0]['address']['addressRegion']
    final_result['state'] = state

    city = data['item'][0]['address']['addressLocality']
    final_result['city'] = city

    fullzips = data['item'][0]['address']['postalCode'].strip()
    final_result['fullzips'] = fullzips

    msa = data['item'][0]['address']['addressLocality']
    final_result['msa'] = msa

    price = data['item'][1]['lowPrice']
    final_result['price'] = price
    final_result['date'] = date

    # Specify your output file name
    output_file = 'beazer_homes.csv'
    with open(output_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=['product_num', 'brand', 'url', 'type', 'title', 'community', 'market',
                                            'state', 'city', 'fullzips', 'msa', 'price', 'date'])
        # writer.writeheader()
        writer.writerows([final_result])
    print(parsed_dict)
