from bs4 import BeautifulSoup
from collections import Counter

# Read HTML content from a text file
with open('index.html', 'r', encoding='utf-8') as file:
    htmll_ = file.read()

colour_mapping = {"fill: rgb(75, 101, 37); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Future Development",
                  "fill:#F7B9D4;stroke:#767669;stroke-width:0.25;stroke-miterlimit:10;": "FD",
                  "fill: rgb(207, 93, 86); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Sold",
                  "fill: rgb(243, 231, 186); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Quick Delivery",
                  "fill: rgb(34, 31, 32); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Closed",
                  "fill: rgb(255, 255, 255); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Unavailable",
                  "fill: rgb(169, 154, 196); stroke: rgb(118, 118, 105); stroke-width: 0.25; stroke-miterlimit: 10;": "Sales Model"}


soup = BeautifulSoup(htmll_, 'html.parser')
# Find all 'g' elements with id starting with 'Symbol' inside 'Lots'
symbols = soup.find('g', id='Lots').find_all('g', id=lambda x: x and x.startswith('Symbol'))

colour_scheme = []
# Loop through each symbol to extract data
for symbol in symbols:
    try:
        lot_id = symbol['data-lotid']
        event_bus_key = symbol['data-eventbuskey']

        path = symbol.find('path') or symbol.find('polygon') or symbol.find('rect')
        if path and 'style' in path.attrs:
            path_data = path['style']
            if path_data:
                colour_scheme.append(path_data)
                # print(f"Lot ID: {lot_id}, EventBus Key: {event_bus_key}")
                # print(f"Path Data: {path_data}")
                # print("path data available\n")
            else:
                print("no path data\n")
        else:
            print("no path \n")

    except Exception as e:
        pass

print(len(colour_scheme))
# Using Counter to count the occurrences
count_dict = Counter(colour_scheme)

# Convert the Counter object to a dictionary (optional)
count_dict = dict(count_dict)

# Create a new dictionary with updated keys
updated_dict = {colour_mapping.get(key, key): value for key, value in count_dict.items()}

# Print the result
print(updated_dict)