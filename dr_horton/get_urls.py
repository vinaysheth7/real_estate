import requests
import xml.etree.ElementTree as ET

# Fetch the XML content from the sitemap URL
sitemap_url = "https://www.drhorton.com/sitemaps/website.xml"
response = requests.get(sitemap_url)
xml_content = response.content

# Parse the XML content
root = ET.fromstring(xml_content)

all_urls = []
# Find all <loc> tags and print their text (URLs)
for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
    url = loc.text
    if url.count("/") > 7:
        all_urls.append(url)

# Specify the file path where you want to write the list
file_path = "horton_urls_july.txt"

# Open the file in write mode and write each element of the list on a separate line
with open(file_path, 'w') as file:
    for element in all_urls:
        file.write(str(element) + '\n')
