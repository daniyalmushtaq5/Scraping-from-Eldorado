import requests
from constant import *

def fetch_offers(game_name, page_num=1, game_count=0, rank_count=0, offers_list=None, search_count=0):

    if offers_list is None:
        offers_list = []

    if isinstance(games_dict[game_name]["search_query"], list):
        search_list_len = len(games_dict[game_name]["search_query"])
        try:
            search_query = games_dict[game_name]["search_query"][search_count]
        except:
            return offers_list
    else:
        search_query = games_dict[game_name]["search_query"]

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
        'searchQuery': search_query,
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

        if page_num <= total_pages and game_count < ITEMS_PER_GAME:
            for offer in data['results']:
                feedback_score = float(offer['userOrderInfo']['feedbackScore'])
                if feedback_score > 99:
                    title = offer['offer'].get('offerTitle', 'N/A')
                    description = offer['offer'].get('description', 'N/A')
                    try:
                        price = int(offer['offer']['pricePerUnitInUSD']['amount'])
                    except (KeyError, TypeError):
                        price = "N/A"
                    try:
                        game_link = f"https://www.eldorado.gg/{offer['offer']['gameSeoAlias']}/oa/{offer['offer']['id']}"
                    except (KeyError, TypeError):
                        game_link = "N/A"

                    server, rank, device = games_dict[game_name]['extract_info'](offer,search_query)
                    if any(value == "N/A" for value in [server, rank, device]):
                        continue
                    
                    if (game_name in ['Valorant', 'League of Legends'] and rank == "Other") or \
                    (game_name == "Call of Duty" and (server == "Warzone 3" or device not in ['PC', 'PSN', 'Xbox'])):
                        continue

                    table = {
                        'Game': game_name,
                        'Field-1': server,
                        'Field-2': rank,
                        'Field-3': device,
                        'Title': title,
                        'DES': description,
                        'Price': price,
                        'Game Link': game_link,
                        'Done': False
                    }

                    offers_list.append(table)
                    game_count += 1
                    rank_count +=1

                if game_count >= ITEMS_PER_GAME:
                    print(f"{ITEMS_PER_GAME} offers are scraped")
                    return offers_list
                
                if rank_count >= RANK_PER_GAME and game_name not in ['GTA 5 Online', 'OS', 'Clash of Clans']:
                    print(f"{RANK_PER_GAME} offers are scraped")
                    # print(f"Search Count : {search_count}")
                    return fetch_offers(game_name, 1, game_count, 0, offers_list, search_count+1)

                
            return fetch_offers(game_name, page_num + 1, game_count, rank_count, offers_list, search_count)
        else:
            print(f"All pages processed or {ITEMS_PER_GAME} offers scraped")
            # print(f"Search Count : {search_count}")
            if isinstance(games_dict[game_name]["search_query"], list) and search_count < search_list_len - 1:
                return fetch_offers(game_name, 1, game_count, rank_count, offers_list, search_count+1)

    else:
        print(f"Error fetching data. Status code: {response.status_code}")

    return offers_list

