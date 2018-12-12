import numpy as np
import pandas as pd
from datetime import datetime
from colorama import init, Fore, Back, Style
import os
clear = lambda: os.system('cls')
init()

#Load the data :
villes = pd.read_csv("villes_france.csv", delimiter=",")

#Nom des colonnes :
villes.columns = ["city_number", "Department", "lower_case_city_name",
"capitalized_city_name",  "streamlined_city_name", "titled_city_name", "soundex",
"metaphone", "zip_code", "dpt_city_number", "INSEE_code", "district", "canton", "unkwown_0", "Population2010",
"1999_Population", "2012_Population", "2010_density", "Area", "grd_geolocalization",
"grs_geolocalization", "unkwown_1", "unkwown_2", "unkwown_3", "unkwown_4", "altitude", "unkwown_5"]

#Fonction :
def nb_of_towns (high):
    number_of_cities_above = (villes[villes.altitude > int(high)].lower_case_city_name.count())
    number_of_cities_under = (villes[villes.altitude < int(high)].lower_case_city_name.count())
    print(Fore.CYAN + "")
    print("\nThere are {} cities above and {} cities under {} meters high".format(number_of_cities_above, number_of_cities_under, answer))
    
    sum_poplation_above = (villes[villes.altitude > int(high)].Population2010.sum())
    sum_poplation_under = (villes[villes.altitude < int(high)].Population2010.sum())
    print(Fore.MAGENTA + "")
    print("There are {} people leaving above and {} people leaving under {} meters high".format(sum_poplation_above, sum_poplation_under, answer))

    try :
        average_population = int((villes[villes.altitude > int(high)].Population2010.mean()))
        print(Fore.RED + "")
        print("There are {} people in average per city leaving above {} meters high".format(average_population, answer))
    except ValueError :
        print(Fore.RED + "")
        print("No average possible with {} meters high".format(answer))

#Loop of the program :
print(Fore.GREEN +"")
Choice_to_continue = input("Do you want to start ? :\n").lower()[0]
while True :
    try :
        if Choice_to_continue == "n" :
            print(Fore.RED + "\n\n\n\n\n\n\nOk, Good by ! :)")
            print(Fore.RED + "{:%Y-%B-%d}".format(datetime.now()))
            break
        elif Choice_to_continue == "y" :
            answer = input("Thanks to comfirm an altitude :\n")
            nb_of_towns (answer)
            print(Fore.GREEN +"")
            Choice_to_continue = input("Do you want to continue ? :\n").lower()[0]
        else : Choice_to_continue = input("Please just say Yes or No :\n").lower()[0]
    except ValueError :
        print("Oh, no we ran into an issue.")
        Choice_to_continue = input("Please just say Yes or No :\n").lower()[0]