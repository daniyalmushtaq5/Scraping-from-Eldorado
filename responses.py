import requests
from constant import games


def response(game_id : int, page_num = 1, count = 0):

    session = requests.Session()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    params = {
        'pageSize': '50',
        'pageIndex': page_num,
        'itemTreeId': f'{game_id}-1-0',
        'offerType': 'Account',
        'deliveryTime': 'Instant',
        'offerSortingCriterion': 'Price',
        'isAscending': 'false',
    }

    response = session.get('https://www.eldorado.gg/api/flexibleOffers/', params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # for page in range(2,len(data['totalPages']) + 1):
        if page_num <= len(data['totalPages']):
            for offer in data['results']:
                if float(offer['userOrderInfo']['feedbackScore']) > 99:
                    try:
                        title = offer['offer']['offerTitle']
                    except(TypeError,KeyError):
                        title = "N/A"
                    try:
                        price = offer['offer']['pricePerUnitInUSD']['amount']
                    except(TypeError,KeyError):
                        price = "N/A"
                    game_name['extract_info'](offer)
                    
                    print(len(data['results']))
                    print(data['totalPages'])
                    count += 1
            if count <= 100:
                response(game_id, page_num + 1, count)
            else:
                print("100 offers are scraped")

        else:
            print("All Pages Done")
    else:
            print("Get Response Error")


if __name__ == "__main__":
    response(16,1)