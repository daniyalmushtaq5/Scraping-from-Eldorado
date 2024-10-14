from constant import games_dict
from responses import fetch_offers
import pandas as pd

def main():
    all_offers = []
    for game_name in games_dict:
        print(f"Game name: {game_name}")
        offers = fetch_offers(game_name)
        print(f"Scraped offers for {game_name}:")
        print(offers)
        all_offers.extend(offers)

    df = pd.DataFrame(all_offers)
    df.to_excel("games_data.xlsx", index=False)

if __name__ == "__main__":
    main()