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
    get_info_for_overwatch
)

MIN_PRICE = 5
MAX_PRICE = 100

games_dict = {
    "Valorant" : {
        "game_id" : '32-1',
        "extract_info" : get_info_for_valorant,
    },
    "FN" : {
        "game_id" : '16-1',
        "extract_info" : get_info_for_fortnite,
    },
    "GTA 5 Online" : {
    "game_id" : '25-1',
    "extract_info" : get_info_for_gta,
    },
    "Tom Clancys Rainbow Six Siege" : {
    "game_id" : '48-1',
    "extract_info" : get_info_for_rainbow_six_siege,
    },
    "Call of Duty" : {
    "game_id" : '35-1',
    "extract_info" : get_info_for_call_of_duty,
    },
    "OS" : {
    "game_id" : '10-1',
    "extract_info" : get_info_for_os,
    },
    "League of Legends" : {
    "game_id" : '17-1',
    "extract_info" : get_info_for_LOL,
    },
    "RBL" : {
    "game_id" : '70-1',
    "extract_info" : get_info_for_roblox,
    },
    "Clash Of Clans (Global)" : {
    "game_id" : '18-1',
    "extract_info" : get_info_for_coc,
    },
    "Overwatch 2" : {
    "game_id" : '27-0',
    "extract_info" : get_info_for_overwatch,
    },
}
