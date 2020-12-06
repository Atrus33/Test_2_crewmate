#get_volleyball_player
#get_team
#get_height
#get_year
#get_nationality #sofijackson

search_name = input("Provide name and surname of the player")

def player_nationality(NATIONALITY,S_name):
    for nationality, names in NATIONALITY.items():
    if S_name in names:
        return "Her nationality is" + nationality
        
    return "Her nationality is unknown"
    
print(player_natioanlity(NATIONALITY, search_name))




#choose_team
#get_members

