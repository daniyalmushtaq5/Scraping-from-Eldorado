from game_data import COD_server_dict, LOL_server_dict

def get_info_for_valorant(offer):
    try:
        server = offer['offer']['tradeEnvironmentValues'][0]['value'] if offer['offer']['tradeEnvironmentValues'][0]['value'] != "EU/TR/MENA/CIS" else "EU"
    except(KeyError,TypeError):
        server = "N/A"
    try:
        rank = offer['offer']['offerAttributeIdValues'][0]['value']
    except(KeyError,TypeError):
        rank = "N/A"
    try:
        device = offer['offer']['tradeEnvironmentValues'][1]['value']
    except(KeyError,TypeError):
        device = "N/A"
    return server, rank, device


def get_info_for_fortnite(offer):
    server = ""
    rank = "Rank Ready"
    device = ""
    return server, rank, device

def get_info_for_gta(offer):
    server = ""
    rank = ""
    try:
        device = offer['offer']['tradeEnvironmentValues'][0]['value']  if offer['offer']['tradeEnvironmentValues'][0]['value'] != "Xbox Series X/S" else "Xbox Series"
    except(TypeError,KeyError):
        device = "N/A"
    return server, rank, device

def get_info_for_rainbow_six_siege(offer):
    server = ""
    rank = "Unranked"
    try:
        device = offer['offer']['tradeEnvironmentValues'][0]['value']  if offer['offer']['tradeEnvironmentValues'][0]['value'] != "PlayStation" else "PSN"
    except(KeyError,TypeError):
        device = "N/A"
    return server, rank, device

def get_info_for_call_of_duty(offer):
    try:
        server = COD_server_dict[offer['offer']['offerAttributeIdValues'][0]['value']] if offer['offer']['offerAttributeIdValues'][0]['value'] != "Warzone 3" else "N/A"
    except(TypeError,KeyError):
        server = "N/A"
    rank = "Rank Ready"
    try:
        device = offer['offer']['tradeEnvironmentValues'][0]['value']  if offer['offer']['tradeEnvironmentValues'][0]['value'] != "PlayStation" else "PSN"
    except(KeyError,TypeError):
        device = "N/A"
    return server, rank, device


def get_info_for_os(offer):
    server = "Old school"
    rank = ""
    device = ""
    return server, rank, device

def get_info_for_LOL(offer):
    try:
        server = LOL_server_dict[offer['offer']['tradeEnvironmentValues'][0]['value']]
    except(KeyError,TypeError):
        server = "N/A"
    try:
        rank = offer['offer']['offerAttributeIdValues'][0]['value'] if offer['offer']['offerAttributeIdValues'][0]['value'] != "Diamond+" else "Diamond"
    except(KeyError,TypeError):
        rank = "N/A"
    device = ""
    return server, rank, device

def get_info_for_roblox(offer):
    server = "Others"
    rank = ""
    device = ""
    return server, rank, device

def get_info_for_coc(offer):
    server = ""
    rank = ""
    device = ""
    return server, rank, device

def get_info_for_overwatch(offer):
    server = ""
    rank = "UnRanked"
    device = ""
    return server, rank, device


