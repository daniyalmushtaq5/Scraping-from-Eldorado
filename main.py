from constant import games_dict
from responses import fetch_offers
import pandas as pd

def main():
    for game_name in games_dict:
        offers = fetch_offers(game_name)
        print(f"Scraped offers for {game_name}:")
        print(offers)

    df = pd.DataFrame(offers)
    df.to_excel("games_data.xlsx", index=False)

if __name__ == "__main__":
    main()