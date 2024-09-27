from game_data import COD_server_dict, LOL_server_dict

def get_info_for_valorant(offer,search_query):
    try:
        server = offer['offer']['tradeEnvironmentValues'][0]['value'] if offer['offer']['tradeEnvironmentValues'][0]['value'] != "EU/TR/MENA/CIS" else "EU"
    except(KeyError,TypeError):
        server = "N/A"
    try:
        rank = offer['offer']['offerAttributeIdValues'][0]['value'] if offer['offer']['offerAttributeIdValues'][0]['value'].strip() != "Ranked Ready" else "Rank Ready"
    except(KeyError,TypeError):
        rank = "N/A"
    try:
        device = offer['offer']['tradeEnvironmentValues'][1]['value']
    except(KeyError,TypeError):
        device = "N/A"
    return server, rank, device


def get_info_for_fortnite(offer,search_query):
    server = ""
    rank = search_query
    device = ""
    return server, rank, device

def get_info_for_gta(offer,search_query):
    server = ""
    rank = ""
    try:
        device = offer['offer']['tradeEnvironmentValues'][0]['value']  if offer['offer']['tradeEnvironmentValues'][0]['value'] != "Xbox Series X/S" else "Xbox Series"
    except(TypeError,KeyError):
        device = "N/A"
    return server, rank, device

def get_info_for_rainbow_six_siege(offer,search_query):
    server = ""
    rank = search_query
    try:
        device = offer['offer']['tradeEnvironmentValues'][0]['value']  if offer['offer']['tradeEnvironmentValues'][0]['value'] != "PlayStation" else "PSN"
    except(KeyError,TypeError):
        device = "N/A"
    return server, rank, device

def get_info_for_call_of_duty(offer,search_query):
    try:
        server = COD_server_dict[offer['offer']['offerAttributeIdValues'][0]['value']]
    except:
        server = "N/A"
    rank = search_query
    try:
        device = offer['offer']['tradeEnvironmentValues'][0]['value']  if offer['offer']['tradeEnvironmentValues'][0]['value'] != "PlayStation" else "PSN"
    except(KeyError,TypeError):
        device = "N/A"
    return server, rank, device


def get_info_for_os(offer,search_query):
    server = "Old school"
    rank = ""
    device = ""
    return server, rank, device

def get_info_for_LOL(offer,search_query):
    try:
        server = LOL_server_dict[offer['offer']['tradeEnvironmentValues'][0]['value']]
    except(KeyError,TypeError):
        server = "N/A"
    try:
        rank = offer['offer']['offerAttributeIdValues'][0]['value'] if offer['offer']['offerAttributeIdValues'][0]['value'] != "Diamond+" else "Diamond"
    except:
        rank = "N/A"
    device = ""
    return server, rank, device

def get_info_for_roblox(offer,search_query):
    server = "Others"
    rank = search_query
    device = ""
    return server, rank, device

def get_info_for_coc(offer,search_query):
    server = ""
    rank = ""
    device = ""
    return server, rank, device

def get_info_for_overwatch(offer,search_query):
    server = ""
    rank = search_query
    device = ""
    return server, rank, device


