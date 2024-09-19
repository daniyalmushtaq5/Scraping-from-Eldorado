from utils import (
    get_info_for_valorant,
    get_info_for_fortnite,
    get_info_for_gta,
    get_info_for_rainbow_six_siege,
    get_info_for_call_of_duty,
    get_info_for_os,
    get_info_for_LOL,
    get_info_for_roblox,
    get_info_for_coc,
    get_info_for_overwatch,
)

MIN_PRICE = 5
MAX_PRICE = 100
ITEMS_PER_GAME = 100

games_dict = {
    "Valorant": {
        "game_id": "32-1",
        "extract_info": get_info_for_valorant,
        "search_query": "",
    },
    "FN": {
        "game_id": "16-1",
        "extract_info": get_info_for_fortnite,
        "search_query": [
            "Unreal",
            "Elite",
            "Platinum",
            "Silver",
            "UnRanked",
            "Fresh New",
            "Champion",
            "Diamond",
            "Gold",
            "Bronze",
            "Rank Ready",
        ],
    },
    "GTA 5 Online": {
        "game_id": "25-1",
        "extract_info": get_info_for_gta,
        "search_query": "",
    },
    "Tom Clancys Rainbow Six Siege": {
        "game_id": "48-1",
        "extract_info": get_info_for_rainbow_six_siege,
        "search_query": [
            "Champions",
            "Emerald",
            "Gold",
            "Bronze",
            "Unranked",
            "Fresh New",
            "Diamond",
            "Platinum",
            "Silver",
            "Copper",
            "Rank Ready",
        ],
    },
    "Call of Duty": {
        "game_id": "35-1",
        "extract_info": get_info_for_call_of_duty,
        "search_query": [
            "Top 250",
            "Crimson",
            "Platinum",
            "Silver",
            "UnRanked",
            "Fresh New",
            "Iridescent",
            "Diamond",
            "Gold",
            "Bronze",
            "Rank Ready",
        ],
    },
    "OS": {
        "game_id": "10-1",
        "extract_info": get_info_for_os,
        "search_query": "",
    },
    "League of Legends": {
        "game_id": "17-1",
        "extract_info": get_info_for_LOL,
        "search_query": "",
    },
    "RBL": {
        "game_id": "70-1",
        "extract_info": get_info_for_roblox,
        "search_query": [
            "A Dusty Trip",
            "Adopt Me",
            "All Star Tower Defence",
            "Anime Adventures",
            "Anime Champions Simulator",
            "Anime Defenders",
            "Anime Fighters Simulator",
            "Anime Last Stand",
            "Anime Racing 2",
            "Anime Simulator",
            "Basketball Legends",
            "BedWars"
        ],
    },
    "Clash of Clans": {
        "game_id": "18-1",
        "extract_info": get_info_for_coc,
        "search_query": "",
    },
    "Overwatch 2": {
        "game_id": "27-0",
        "extract_info": get_info_for_overwatch,
        "search_query": [
            "Top 500",
            "Grandmaster",
            "Master",
            "Diamond",
            "Platinum",
            "Gold",
            "Silver",
            "Bronze",
            "UnRanked",
            "Rank Ready",
            "Fresh New"
        ],
    },
}
