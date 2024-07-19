from bs4 import BeautifulSoup

import requests
import xml.etree.ElementTree as ET


def get_all_states():
    url = "https://www.lgihomes.com/map-search"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'shell#lang=en; ASP.NET_SessionId=nraorj33repvb2ebqm3qzq3s; sxa_site=BrandSite-Public; SC_ANALYTICS_GLOBAL_COOKIE=e3e57ecc061f418fb859bd56d5186a34|True; _gcl_au=1.1.616895084.1715600447; _ga=GA1.1.115600391.1715600448; lm_ct=true; viewer_token=18f71c15dfa; lm_ssid=v4afhkhhaajehdhjahbbhbfgaaeekabh; _clck=zh170a%7C2%7Cflq%7C0%7C1594; _fbp=fb.1.1715600454955.325777614; invoca_session=%7B%22ttl%22%3A%222024-06-12T11%3A40%3A55.448Z%22%2C%22session%22%3A%7B%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Atrue%7D%7D; __RequestVerificationToken=w2xASOxuhp5pJgsUTX2unoDuUdkIpf9esa7gG-H1V-HVpEyU8Ym9WoATCppOCWCt0VFW8lszl94TGyqk912l3eNOO17ucnHKyVdc1ybFoDw1; lgi_resume_journey_community={9772174e-1f23-47cd-b46c-03961e75177d}; session_pages=2; lgi_resume_journey_floorplan={afeaaa7c-e570-441f-bb84-a73884f27781}; _ga_0K4FHKH8XV=GS1.1.1715600447.1.1.1715600988.60.0.849063102; _uetsid=a4483ab0111d11efbf6d4f589a2e8f91; _uetvid=a4484ef0111d11efb05bc74a21446f25; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNjAzMTQ4YmItYjRjMC00ZTU4LWIxYjctNGZkYTI4MjUzMjk4JTIyJTJDJTIyZSUyMiUzQTE3MTYxMjY1OTEzODclN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyYWRkNmUxNzktNzk2Ni00YzAwLTljYTAtNWMyZGFlNzYzYmVlJTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTcxNTYwMjc5MTg5NyU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNjFkMjFkNjktYjhjOS00Zjk0LTg1ZmQtN2ZiMmJmYjZmOWY4JTIyJTJDJTIyZSUyMiUzQTE3MTYxMjY1OTEzODklN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMTElMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNzE1NjAyNzkxODk3JTdEJTJDJTIyTUdYX0VJRCUyMiUzQSU3QiUyMnYlMjIlM0ElMjJuc19zZWdfMDAwJTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTcxNTYwMjc5MTg5NyU3RCU3RA==; _clsk=1owutgx%7C1715601000907%7C11%7C1%7Cw.clarity.ms%2Fcollect; sxa_site=BrandSite-Public',
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

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all 'a' tags within 'li' tags with class 'marketslist-areas-city'
    li_elements = soup.find_all('li', class_='marketslist-areas-city')

    # Extract href attributes from each 'a' tag
    href_list = ['https://www.lgihomes.com' + a['href'] + '/' for li in li_elements for a in li.find_all('a')]

    print(href_list)

    return href_list


def get_all_city_utls():
    url = "https://www.lgihomes.com/sitemap.xml"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'EPiStateMarker=true; ARRAffinity=4ab65a0346cca8a3aa76d4918984fb5bba5a7ce0188d2e173bcc9dbcb1d36bd2; ARRAffinitySameSite=4ab65a0346cca8a3aa76d4918984fb5bba5a7ce0188d2e173bcc9dbcb1d36bd2; ai_user=NnFn0j/t0ysCfm6E4wFLnl|2024-04-30T10:48:20.291Z; atlasvid=%7B%22visitorid%22%3A%2260e7ccc8-77ad-449d-b15d-bfac0410ac33%22%7D; msd365mkttr=dyt5eg76XxXeUvqOhQIrea6glQ73TXZCksTEYP8X; msd365mkttrs=UOiHbsAt; kbh.recent.region=14; .AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8IUWs55mejhPpKk6ZBC8-LvSwXjzoYuXODdP7L_K-A38sRpYePIegHEftTxC7Tn82Lg_sCwEF4mRysWW6VUWaKceOr7ShDuHkXEA5eOBvPJHGRmCwis8Z2OhNb2rmdYZmk4POPCSgJA5VzVVQFZq6Kw; atlasseg_575bd48a7531400885414037bfb89219=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.kbhome.com%2F%22%2C%22srcUrl%22%3A%22https%3A%2F%2Fwww.kbhome.com%2Fnew-homes-phoenix%22%2C%22division%22%3A%22Phoenix%22%2C%22community%22%3Anull%2C%22plan%22%3Anull%2C%22source%22%3Anull%2C%22medium%22%3Anull%2C%22campaign%22%3Anull%7D; _vwo_uuid_v2=D91E3030D7F14288A22127B066E4A819C|4bc119db5c83116c4d70b836d446f2fd; _hjSessionUser_139514=eyJpZCI6ImUwMDhkOGVhLTQ1NjEtNTMxMi1iNzU4LWUzOWUzZTBhZjQ3MiIsImNyZWF0ZWQiOjE3MTUzMzQzNzI4ODUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_139514=eyJpZCI6IjMxYmYzNDkwLThhODktNDQ2ZS04NmYzLTI0YmU0NDkzNzQzMCIsImMiOjE3MTUzMzQzNzI4ODUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _bts=7aa5f05d-fc24-4589-bca1-f8402357db70; _gcl_au=1.1.583398162.1715334374; _fbp=fb.1.1715334374147.756274761; _pin_unauth=dWlkPVlqRXdPREF5TURJdE1EUXpaaTAwTlRabExXSXpabUl0WlRWbVlUY3paRFV4T1Rrdw; _gid=GA1.2.800245453.1715334377; _bti=%7B%22app_id%22%3A%22kb-home%22%2C%22bsin%22%3A%22VE2fD9n3bu%2Frlrd3zXPsc%2FpJM0lejW5glBCoaeEaruqTTcgcZhGI44sXdCcUUjghgLIGO1u7%2FNLO%2BA8nmnCcdA%3D%3D%22%2C%22is_identified%22%3Afalse%7D; utag_main=v_id:018f2e9ea80c001e479e924194cd05075001706d00942$_sn:2$_se:16$_ss:0$_st:1715336368605$dc_visit:2$ses_id:1715334371894%3Bexp-session$_pn:6%3Bexp-session$dc_event:14%3Bexp-session$pre_page:%2Fnew-homes-san-antonio%2Fwillow-view%2Fmir%3Bexp-session$dc_region:us-west-2%3Bexp-session; _ga_KG7636GCER=GS1.1.1715334374.1.1.1715334568.58.0.0; ai_session=Ui7AVoWvqg2cZBV6IGqXmi|1715334370456|1715334569859; _ga=GA1.2.1350967677.1715334374',
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

    xml_content = response.content
    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Extract all 'loc' elements and store their text in a list
    urls = [url.text for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

    print(urls)
    return urls


def filter_urls():
    all_states = get_all_states()
    print("total_states", len(all_states))

    all_urls = get_all_city_utls()
    print("total_urls", len(all_urls))

    all_home_locations = [url for url in all_urls if any(html_url in url for html_url in all_states)]

    # Specify the file path where you want to write the list
    file_path = "lgi_home_urls.txt"

    # Open the file in write mode and write each element of the list on a separate line
    with open(file_path, 'w') as file:
        for element in all_home_locations:
            file.write(str(element) + '\n')


filter_urls()
