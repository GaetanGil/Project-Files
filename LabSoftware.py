from datetime import datetime
from colorama import init, Fore, Back, Style
import os
clear = lambda: os.system('cls')
init()


cost_sauce_1 = 0.25
cost_sauce_2 = 0.50

Sauce_1_order = 0
Sauce_2_order = 0

total_cost_sauce_1 = 0
total_cost_sauce_2 = 0

Prix_Petite = 3
Prix_Moyenne = 4
Prix_Grande = 5

Petite_Order = 0
Moyenne_Order = 0
Grande_Order = 0

Petit_Menu = 0
Moyen_Menu = 0
Grand_Menu = 0

Drink_order = 0
Desert_order = 0

Lydia = 0
Carte = 0
Espece = 0

def askDrink():
    print(Fore.CYAN + "")
    Choice_Drink = input("Any drink? :\n").lower()[0]
    while True :
        try :
            if Choice_Drink == "n" :
                return 0
            elif Choice_Drink == "y" :
                return 1
            else : Choice_Drink = input("Please just say yes or no :\n").lower()[0]
        except ValueError :
            print("Oh, no we ran into an issue.")
            Choice_Drink = input("Please just say 1 or 2 :\n").lower()[0]

def askDesert():
    print(Fore.MAGENTA + "")
    Choice_Desert = input("Any desert? :\n").lower()[0]
    while True :
        try :
            if Choice_Desert == "n" :
                return 0
            elif Choice_Desert == "y" :
                return 1
            else : Choice_Desert = input("Please just say yes or no :\n").lower()[0]
        except ValueError :
            print("Oh, no we ran into an issue.")
            Choice_Desert = input("Please just say 1 or 2 :\n").lower()[0]

def Conclusion():
    print(Fore.RED + "\n\n{:%Y-%B-%d}".format(datetime.now()))
 
    print("\n{} Small menu ordered".format(Petit_Menu))
    print("{} Big menu ordered".format(Moyen_Menu))
    print("{} Giant menu ordered".format(Grand_Menu))

    print("\n{} Small boxes ordered".format(Petite_Order))
    print("{} Big boxes ordered".format(Moyenne_Order))
    print("{} Giant boxes ordered".format(Grande_Order))

    print("\n{} Drinks ordered".format(Drink_order))
    print("{} Deserts ordered".format(Desert_order))

    print("\n{} of sauce 1 has been ordered for a total of {} €".format(Sauce_1_order, total_cost_sauce_1))
    print("{} of sauce 2 has been ordered for a total of {} €".format(Sauce_2_order, total_cost_sauce_2))

    print("\n{} Lydias".format(Lydia))
    print("{} Credit card payments".format(Carte))
    print("{} Cash payments".format(Espece))


Program = True
while Program :
    Size = True
    print(Fore.GREEN +"")
    Choice_size = input("""
    
What is the size of the box : \nPlease choose between\ns\tb\tg\n""")
    while Size :
        if Choice_size == "s" :
            Small_Menu = True
            print(Fore.YELLOW + "")
            Choice_menu = input("Menu? :\n").lower()[0]
            while Small_Menu :
                try :
                    if Choice_menu == "n" :
                        Drink_order += askDrink()
                        Desert_order += askDesert()                       

                        Petite_Order += 1
                        break
                    elif Choice_menu == "y" :
                        Petit_Menu += 1
                        break
                    else : Choice_menu = input("Please just say yes or no :\n").lower()[0]
                except ValueError :
                    print("Oh, no we ran into an issue.")
                    Choice_menu = input("Please just say yes or no :\n").lower()[0]
            break
        elif Choice_size == "b" :
            Big_Menu = True
            print(Fore.YELLOW + "")
            Choice_menu = input("Menu? :\n").lower()[0]
            while Big_Menu :
                try :
                    if Choice_menu == "n" :
                        Drink_order += askDrink()
                        Desert_order += askDesert()   
                        Moyenne_Order += 1
                        break
                    elif Choice_menu == "y" :
                        Moyen_Menu += 1
                        break
                    else : Choice_menu = input("Please just say yes or no :\n").lower()[0]
                except ValueError :
                    print("Oh, no we ran into an issue.")
                    Choice_menu = input("Please just say yes or no :\n").lower()[0]
            break
        elif Choice_size == "g" :
            Giant_Menu = True
            print(Fore.YELLOW +  "")
            Choice_menu = input("Menu? :\n").lower()[0]
            while Giant_Menu :
                try :
                    if Choice_menu == "n" :
                        Drink_order += askDrink()
                        Desert_order += askDesert()

                        Grande_Order += 1
                        break
                    elif Choice_menu == "y" :
                        Grand_Menu += 1
                        break
                    else : Choice_menu = input("Please just say yes or no :\n").lower()[0]
                except ValueError :
                    print("Oh, no we ran into an issue.")
                    Choice_menu = input("Please just say yes or no :\n").lower()[0]
            break
        else :
            print("Oh, no we ran into an issue.")
            Choice_size = input("Please choose between\ns\tb\tg\n")

    Sauce = True
    print(Fore.BLUE + "")
    Choice_Sauce = input("Which sauce? :\n")
    while Sauce :
        try :
            if int(Choice_Sauce) == 1 :
                Sauce_1_order += 1
                total_cost_sauce_1 = cost_sauce_1 * Sauce_1_order
                break
            elif int(Choice_Sauce) == 2 :
                Sauce_2_order += 1
                total_cost_sauce_2 = cost_sauce_2 * Sauce_2_order
                break
            else : Choice_Sauce = input("Please just say 1 or 2 :\n")
        except ValueError :
            print("Oh, no we ran into an issue.")
            Choice_Sauce = input("Please just say 1 or 2 :\n")

    Payment = True
    print(Fore.BLUE + "")
    Choice_Payment = input("Which payment method? :\n")
    while Payment :
        try :
            if Choice_Payment == "c" :
                Carte += 1
                break
            elif Choice_Payment == "l" :
                Lydia += 1
                break
            elif Choice_Payment == "e" :
                Espece += 1
                break
            else : Choice_Payment = input("Please choose between\nc\tl\te\n").lower()[0]
        except ValueError :
            print("Oh, no we ran into an issue.")
            Choice_Payment = input("Please choose between\nc\tl\te\n").lower()[0]

    End_of_service = True
    print(Fore.YELLOW + "")
    Choice_End = input("End of the service?\n").lower()[0]
    while End_of_service :
        try :
            if Choice_End == "n" :
                break
            elif Choice_End == "y" :
                Choice_Certain = input("ARE YOU SURE THIS IS THE END?\n").lower()[0]
                if Choice_Certain == "y" :
                    Program = False
                else : break
                break
            else : Choice_End = input("Please just say yes or no :\n").lower()[0]
        except IndexError :
            print("Oh, no we ran into an issue.")
            Program = input("\nIs it the end of the service?\nPlease just say yes or no :\n").lower()[0] in ["n"," "]

Conclusion()