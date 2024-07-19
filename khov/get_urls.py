import requests
import xml.etree.ElementTree as ET

sitemap_url = ['https://www.khov.com/services/homesitemap/10/0',
               'https://www.khov.com/services/homesitemap/10/10',
               'https://www.khov.com/services/homesitemap/10/20',
               'https://www.khov.com/services/homesitemap/10/40',
               'https://www.khov.com/services/homesitemap/10/50',
               'https://www.khov.com/services/homesitemap/10/60',
               'https://www.khov.com/services/homesitemap/10/80',
               'https://www.khov.com/services/homesitemap/10/90',
               'https://www.khov.com/services/homesitemap/10/100',
               'https://www.khov.com/services/homesitemap/10/110',
               'https://www.khov.com/services/homesitemap/10/120',
               'https://www.khov.com/services/homesitemap/10/130',
               'https://www.khov.com/services/homesitemap/10/140',
               'https://www.khov.com/services/homesitemap/10/150',
               'https://www.khov.com/services/homesitemap/10/160']
def get_urls(sitemap_url):
    all_urls = []
    # Fetch the XML content from the sitemap URL
    for site_map in sitemap_url:
        print(site_map)

        response = requests.get(site_map)
        xml_content = response.content

        # Parse the XML content
        root = ET.fromstring(xml_content)

        # Find all <loc> tags and print their text (URLs)
        for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            url = loc.text
            if url.count("/") > 7:
                all_urls.append(url)

    # Specify the file path where you want to write the list
    file_path = "khov_urls_12june.txt"

    # Open the file in write mode and write each element of the list on a separate line
    with open(file_path, 'a') as file:
        for element in all_urls:
            file.write(str(element) + '\n')

get_urls(sitemap_url)
