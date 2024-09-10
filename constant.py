from  utils import *

games_dict = {
    "Valorant" : {
        "game_id" : '32-1',
        "extract_info" : get_info_for_valorant,
    },
    "Fortnite" : {
        "game_id" : '16-1',
        "extract_info" : get_info_for_fortnite,
    },
    "GTA 5" : {
    "game_id" : '25-1',
    "extract_info" : get_info_for_gta,
    },
    "Rainbow Six Siege" : {
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
    "Roblox" : {
    "game_id" : '70-1',
    "extract_info" : get_info_for_roblox,
    },
    "COC" : {
    "game_id" : '18-1',
    "extract_info" : get_info_for_coc,
    },
    "Overwatch 2" : {
    "game_id" : '27-0',
    "extract_info" : get_info_for_overwatch,
    },
}

COD_server_dict = {
    "Cold War" : "Black Ops Cold War",
    "Modern Warfare I" : "Modern Warfare",
    "Modern Warfare II" : "Modern Warfare 2",
    "Modern Warfare III" : "Modern Warfare 3",
    "Other" : "Others",
    "Vanguard" : "Vanguard",
    "Warzone 3" : ""
}

LOL_server_dict = {
    "Brazil" : "BR",
    "Europe Nordic & East" : "EUNE",
    "PBE" : "PBE",
    "Singapore" : "SG",
    "Philippines" : "PH",
    "Vietnam" : "VN",
    "Thailand" : "TH",
    "Taiwan" : "TW",
    "Middle East" : "ME",
    "Europe West" : "EUW",
    "Latin America North": "LAN",
    "Latin America South": "LAS",
    "Oceania": "OCE",
    "Russia": "RU",
    "Turkey": "TR",
    "Japan": "JP"
}

