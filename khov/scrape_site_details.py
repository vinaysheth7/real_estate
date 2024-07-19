import csv
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from collections import Counter

colour_mapping = {
    "fill: rgb(75, 101, 37); stroke: rgb(118, 118, 105);": "Future Development",
    "fill:#F7B9D4;stroke:#767669;stroke-width:0.25;stroke-miterlimit:10;": "FD",
    "fill: rgb(207, 93, 86); stroke: rgb(118, 118, 105);": "Sold",
    "fill: rgb(243, 231, 186); stroke: rgb(118, 118, 105);": "Quick Delivery",
    "fill: rgb(34, 31, 32); stroke: rgb(118, 118, 105);": "Closed",
    "fill: rgb(34, 31, 32); stroke: rgb(118, 118, 105); stroke-miterlimit: 10;": "Closed",
    "fill: rgb(255, 255, 255); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Unavailable",
    "fill: rgb(169, 154, 196); stroke: rgb(118, 118, 105);": "Sales Model",
    "fill: rgb(129, 184, 188); stroke: rgb(118, 118, 105);": "Available",
    "fill: rgb(255, 255, 255); stroke: rgb(118, 118, 105);": "Unavailable",
    "fill: rgb(205, 202, 198); stroke: rgb(118, 118, 105);": "Reserved"}

with open('site_plan_v2') as urls:
    result_dict = {}
    urls = list(dict.fromkeys([url.strip() for url in urls]))

# def fetch_site_plans():
#     for url in urls:
#         print(url)
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument(
#             "executable_path=/Users/abhijitkumar/Documents/updated items - work /Work/home_prices/khov/chromedriver")
#
#         # Initialize Selenium WebDriver with Chrome options
#         driver = webdriver.Chrome(options=chrome_options)
#         # Open the website
#         driver.get(url)
#
#         # After clicking, you can continue with other actions or scraping
#         time.sleep(50)
#         # Close the browser
#
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         # Find all 'g' elements with id starting with 'Symbol' inside 'Lots'
#         # symbols = soup.find('g', id='Lots').find_all('g', id=lambda x: x and x.startswith('Symbol'))
#         symbols = soup.find('g', id=lambda x: x and x.startswith('Lots')).find_all('g', id=lambda x: x and x.startswith('Symbol'))
#
#         print(symbols)
#         colour_scheme = []
#         # Loop through each symbol to extract data
#         for symbol in symbols:
#             try:
#                 lot_id = symbol['data-lotid']
#                 event_bus_key = symbol['data-eventbuskey']
#
#                 path = symbol.find('path') or symbol.find('polygon') or symbol.find('rect')
#                 if path and 'style' in path.attrs:
#                     path_data = path['style']
#                     if path_data:
#                         colour_scheme.append(path_data)
#                         # print(f"Lot ID: {lot_id}, EventBus Key: {event_bus_key}")
#                         # print(f"Path Data: {path_data}")
#                         # print("path data available\n")
#                     else:
#                         print("no path data\n")
#                 else:
#                     print("no path \n")
#
#             except Exception as e:
#                 pass
#
#         print(len(colour_scheme))
#         # Using Counter to count the occurrences
#         count_dict = Counter(colour_scheme)
#
#         # Convert the Counter object to a dictionary (optional)
#         count_dict = dict(count_dict)
#
#         # Create a new dictionary with updated keys
#         updated_dict = {colour_mapping.get(key, key): value for key, value in count_dict.items()}
#
#         # Print the result
#         print(updated_dict)
#
#         result = [{url: updated_dict, 'total': len(colour_scheme)}]
#         print(result)
#
#         # Specify your output file name
#         # Open the file in append mode
#         with open('site_details_v2_30may.txt', 'a') as file:
#             for line in result:
#                 file.write(str(line) + '\n')
#
#         colour_scheme.clear()
#         print('\n')


def fetch_site_plans():
    print("statring", len(urls))
    for url in urls[109:]:
        print(url)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
            "executable_path=/Users/abhijitkumar/Documents/updated items - work /Work/home_prices/khov/chromedriver")

        # Initialize Selenium WebDriver with Chrome options
        driver = webdriver.Chrome(options=chrome_options)
        # Open the website
        driver.get(url)

        # Wait for the page to load
        time.sleep(50)

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all 'g' elements with id starting with 'Symbol' inside 'Lots'
        symbols = soup.find('g', id=lambda x: x and x.startswith('Lots')).find_all('g', id=lambda x: x and x.startswith('Symbol'))

        colour_scheme = []
        dimensions_data = []

        # Loop through each symbol to extract data
        for symbol in symbols:
            try:
                lot_id = symbol['data-lotid']
                event_bus_key = symbol['data-eventbuskey']

                path = symbol.find('path') or symbol.find('polygon') or symbol.find('rect')
                path_data = path['style'] if path and 'style' in path.attrs else None
                if path_data:
                    colour_scheme.append(path_data)

                    # Extract dimensions if present
                    dims_id = symbol['id'] + '-dims'
                    dims = soup.find('g', id=dims_id)
                    if dims:
                        dim_texts = dims.find_all('text')
                        dimensions = [text.get_text() for text in dim_texts]

                        # Extract lot number
                        lot_number_g = symbol.find('g', id=lambda x: x and x.startswith('TEXT_'))
                        if lot_number_g:
                            lot_number_text = lot_number_g.find('text').get_text()
                        else:
                            lot_number_text = 'Unknown'
                    else:
                        lot_number_text = 'Unknown'
                        dimensions = ['Not available']

                    dimensions_data.append({lot_number_text: dimensions})

            except Exception as e:
                pass

        # Deduplicate dimensions_data
        unique_dimensions = {}
        for dim in dimensions_data:
            for key, value in dim.items():
                if key not in unique_dimensions:
                    unique_dimensions[key] = value

        dimensions_data = [{key: value} for key, value in unique_dimensions.items()]

        # Using Counter to count the occurrences
        count_dict = Counter(colour_scheme)

        # Convert the Counter object to a dictionary
        count_dict = dict(count_dict)

        # Create a new dictionary with updated keys and add dimensions data
        updated_dict = {colour_mapping.get(key, key): {'count': value, 'dimensions': dimensions_data} for
                        key, value in count_dict.items()}

        # Print the result
        print(updated_dict)

        result = [{url: updated_dict, 'total': len(colour_scheme)}]
        print(result)

        # Append the result to a file
        with open('site_details_v2_30may.txt', 'a') as file:
            for line in result:
                file.write(str(line) + '\n')

        colour_scheme.clear()
        dimensions_data.clear()
        print('\n')


# Function to clean the keys
def clean_key(key):
    # Regex pattern to remove 'stroke-width' and 'stroke-miterlimit' along with their values
    pattern = r'; stroke-width: [^;]+; stroke-miterlimit: [^;]+'
    # Substitute the pattern with an empty string
    cleaned_key = re.sub(pattern, '', key)
    return cleaned_key.strip()


# def parse_site_plans():
#     import ast
#
#     result = []
#     final_dict = {}
#     # Initialize a list to store the dictionaries
#     dictionaries = []
#
#     # Open the file and read it line by line
#     with open('site_details_v2_30may.txt', 'r') as file:
#         for line in file:
#             line = line.strip()  # Remove leading/trailing whitespace
#             if line:  # Ensure the line is not empty
#                 try:
#                     dictionaries.append(ast.literal_eval(line))
#                 except (SyntaxError, ValueError) as e:
#                     print(f"Error parsing dictionary: {e}")
#
#     print(dictionaries[0])
#     # Print the result
#     for d in dictionaries:
#         for k, v in d.items():
#             if k != 'total':
#                 final_dict['url'] = k
#                 final_dict['site_plan'] = {colour_mapping.get(clean_key(key), key): value for key, value in
#                                            v.items()}
#                 result.append(final_dict.copy())
#                 print(final_dict)
#                 # final_dict['site_plan'] = {colour_mapping[clean_key(key)]: value for key, value in v.items()}
#                 # print('\n')
#             #
#             # else:
#             #     final_dict['total'] = v
#             #     print(final_dict)
#             #     result.append(final_dict)
#
#     print(result)
#
#     ##### WRITE TO CSV ######
#     # Define all possible keys in site_plan
#     all_keys = ['Sales Model', 'Closed', 'Quick Delivery', 'Sold', 'Unavailable', 'Future Development', 'Available',
#                 'Reserved']
#
#     # Prepare the list of rows for the CSV
#     rows = []
#
#     for item in result:
#         row = {
#             'url': item['url']
#         }
#         total = 0
#         # Initialize all possible keys with 0 and calculate the total
#         for key in all_keys:
#             value = item['site_plan'].get(key, 0)
#             row[key] = value
#             total += value
#         row['total'] = total
#         rows.append(row)
#
#     # Define CSV column headers
#     fieldnames = ['url'] + all_keys + ['total']
#
#     # Write the rows to a CSV file
#     with open('site_plans_urls_12June.csv', 'w', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)
#
#     print("CSV file created successfully.")

def parse_site_plans():
    import ast
    import csv

    result = []
    final_dict = {}
    # Initialize a list to store the dictionaries
    dictionaries = []

    # Open the file and read it line by line
    with open('site_details_v2_30may.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Ensure the line is not empty
                try:
                    dictionaries.append(ast.literal_eval(line))
                except (SyntaxError, ValueError) as e:
                    print(f"Error parsing dictionary: {e}")

    # Print the result
    for d in dictionaries:
        for k, v in d.items():
            if k != 'total':
                final_dict['url'] = k
                final_dict['site_plan'] = {colour_mapping.get(clean_key(key), key): value for key, value in v.items()}
                result.append(final_dict.copy())
                # print(final_dict)


    ##### WRITE TO CSV ######
    # Define all possible keys in site_plan
    all_keys = ['Sales Model', 'Closed', 'Quick Delivery', 'Sold', 'Unavailable', 'Future Development', 'Available', 'Reserved']

    # Prepare the list of rows for the CSV
    rows = []

    try:
        for item in result:
            row = {
                'url': item['url']
            }
            total = 0
            # Initialize all possible keys with 0 and calculate the total
            for key in all_keys:
                print(item)
                value = item['site_plan'].get(key, {'count': 0, 'dimensions': []})
                row[key] = value['count']
                row[f'{key} dimensions'] = value['dimensions']
                total += value['count']
            row['total'] = total
            rows.append(row)
    except Exception as e:
        print(e)
    # Define CSV column headers
    fieldnames = ['url'] + [f'{key},{key} dimensions' for key in all_keys] + ['total']
    # Flatten the fieldnames list
    fieldnames = [item for sublist in fieldnames for item in sublist.split(',')]

    # Write the rows to a CSV file
    with open('site_plans_urls_12June.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("CSV file created successfully.")


if __name__ == '__main__':
    # fetch_site_plans()
    parse_site_plans()
