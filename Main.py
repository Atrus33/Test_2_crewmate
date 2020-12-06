import sys
from os import system
from time import sleep
import pandas as pd
import argparse

# Definition of positional and optional arguments
parser = argparse.ArgumentParser()

parser.add_argument("dataset_path", help="insert the full path of the dateset")
parser.add_argument("dataset_name", help="insert the name of the dataset file")
parser.add_argument("-t", "--type", choices=["csv", "xlsx"], help="choose the extension of the dataset file")
parser.add_argument("-v", "--verbosity", action="count", help="increase output verbosity")
# -v informazioni aggiuntive per l'utente
# -vv informazioni aggiuntive per l'utente e per lo svilippatore
args = parser.parse_args()
dataset_path = args.dataset_path
dataset_name = args.dataset_name
extension_type = args.type

system('cls')

if args.verbosity is not None:
    print("verbosity turned on")
if args.verbosity == 2:
    print("E' stata scelta l'estensione: ", extension_type)

# Carico il file excel in un dataframe in base al tipo di estensione scelto
if extension_type == "xlsx":
    dataframe_volley = pd.read_excel(dataset_path+"\\"+dataset_name+"."+extension_type)
else:
    dataframe_volley = pd.read_csv(dataset_path + "\\" + dataset_name + "." + extension_type, sep=';', encoding="ISO-8859-1")

if args.verbosity == 2:
    print(dataframe_volley)

def my_input():   
    print('What would you like to search?')
    x = input('Type "A" if you want to know more info about a volleyball player.\nType "B" if you want to know more info about a volleyball team.\nType "Q" if you want to quit the program.\nYour choice is: ')
    return x

# define the function blocks
def info_player():
    print("You chose to have more info about the volleyball player.\n")
    sys.exit("End program")

def info_team():
    print("You chose to have more info about the volleyball team.\n")
    sys.exit("End program")

def my_quit():
    sys.exit("You chose to quit the program.\n")
    
# map the inputs to the function blocks
options = {
    "A" : info_player,
    "B" : info_team,
    "Q" : my_quit,
}

choice = my_input()    
    
while (True):
    if (choice == "A" or choice == "B" or choice == "Q"):
        options[choice]()
    else:
        print("Your choice is not correct!!\n")
        # sleep for 2 seconds after printing output 
        sleep(2)
        system('cls')
        choice = my_input()
