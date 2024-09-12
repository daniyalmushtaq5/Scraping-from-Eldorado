import requests
from constant import *

def fetch_offers(game_name, page_num=1, count=0, offers_list=None):

    if offers_list is None:
        offers_list = []

    session = requests.Session()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    params = {
        'pageSize': '50',
        'pageIndex': page_num,
        'itemTreeId': f'{games_dict[game_name]["game_id"]}-0',
        'offerType': 'Account',
        'lowestPrice': MIN_PRICE,
        'highestPrice': MAX_PRICE,
        'deliveryTime': 'Instant',
        'offerSortingCriterion': 'Price',
        'isAscending': 'false',
    }

    response = session.get('https://www.eldorado.gg/api/flexibleOffers/', params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        total_pages = int(data['totalPages'])

        if page_num <= total_pages and count < ITEMS_PER_GAME:
            for offer in data['results']:
                feedback_score = float(offer['userOrderInfo']['feedbackScore'])
                if feedback_score > 99:
                    title = offer['offer'].get('offerTitle', 'N/A')
                    try:
                        price = int(offer['offer']['pricePerUnitInUSD']['amount'])
                    except(KeyError,TypeError):
                        price = "N/A"
                    try:
                        game_link = f'https://www.eldorado.gg/{offer['offer']['gameSeoAlias']}/oa/{offer['offer']['id']}'
                    except(KeyError,TypeError):
                        game_link = "N/A"

                    server, rank, device = games_dict[game_name]['extract_info'](offer)

                    table = {
                        'Game': game_name,
                        'Field-1': server,
                        'Field-2': rank,
                        'Field-3': device,
                        'Title': title,
                        'DES': title,
                        'Price': price,
                        'Game Link' : game_link,
                        'Delete': False,
                        'Done': False
                    }

                    offers_list.append(table)
                    count += 1

                if count >= ITEMS_PER_GAME:
                    print(f"{ITEMS_PER_GAME} offers are scraped")
                    return offers_list

            return fetch_offers(game_name, page_num + 1, count, offers_list)
        else:
            print(f"All pages processed or {ITEMS_PER_GAME} offers scraped")

    else:
        print(f"Error fetching data. Status code: {response.status_code}")

    return offers_list
