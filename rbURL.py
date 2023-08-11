# -----------------------------------------
# file name     : rbURL.py
# date created  : 23 - december - 2019 
# author        : @rbayuokt
# instagram     : @rbayuokt
# made with ♥ in Cimahi, Jawa Barat , Indonesia
# github        : https://github.com/rbayuokt/rbURL-HomographAttack
# -----------------------------------------

from sys import exit , platform
from os import system
from time import sleep
from colorama import init, Fore, Back, Style

from domain_checker import check_domain

init()

# Cryrillic character look alike to latin character
CryrillicList = ['Cyrillic S',
                'Cyrillic I',
                'Cyrillic A',
                'Cyrillic B',
                'Cyrillic M',
                'Cyrillic H',
                'Cyrillic O',
                'Cyrillic P',
                'Cyrillic C',
                'Cyrillic T',
                'Cyrillic y',
                'Cyrillic a',
                'Cyrillic B',
                'Cyrillic e',
                'Cyrillic m',
                'Cyrillic h',
                'Cyrillic o',
                'Cyrillic p',
                'Cyrillic c',
                'Cyrillic t',
                'Cyrillic y',
                'Cyrillic x',
                'Cyrillic s',
                'Cyrillic i',
                'Cyrillic j']

# Cyrillic unicodes
CyrillicUnicode = ['\u0405',
                    '\u0406',
                    '\u0410',
                    '\u0412',
                    '\u041C',
                    '\u041D',
                    '\u041E',
                    '\u0420',
                    '\u0421',
                    '\u0422',
                    '\u0423',
                    '\u0430',
                    '\u0432',
                    '\u0435',
                    '\u043C',
                    '\u043D',
                    '\u043E',
                    '\u0440',
                    '\u0441',
                    '\u0442',
                    '\u0443',
                    '\u0445',
                    '\u0455',
                    '\u0456',
                    '\u0458']

# Greek character look alike to latin character
GreekList = ['Greek J',
            'Greek A',
            'Greek B',
            'Greek E',
            'Greek Z',
            'Greek H',
            'Greek I',
            'Greek K',
            'Greek M',
            'Greek N',
            'Greek O',
            'Greek P',
            'Greek T',
            'Greek Y',
            'Greek X',
            'Greek i',
            'Greek k',
            'Greek v',
            'Greek o',
            'greek u',
            'Greek c',
            'Greek j']

# Greek unicodes
GreekUnicode = ['\u037F',
                '\u0391',
                '\u0392',
                '\u0395',
                '\u0396',
                '\u0397',
                '\u0399',
                '\u039A',
                '\u039C',
                '\u039D',
                '\u039F',
                '\u03A1',
                '\u03A4',
                '\u03A5',
                '\u03A8',
                '\u03B9',
                '\u03BA',
                '\u03BD',
                '\u03BF',
                '\u03C5',
                '\u03F2',
                '\u03F3']

RED, WHITE, GREEN, END, YELLOW , BOLD = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m' , '\033[1m'

# clear the screen for linux , mac , windows
def clear():
    if platform == 'linux' or platform == 'linux2':
        system('clear')
    elif platform == 'darwin':
        system('clear')
    elif platform == 'win32':
        system('cls')

# WELCOME MESSAGE 
# Sorry if my english are bad :( 
# I'm trying my best for explain this source code
def salam():
    print(Fore.RED+'''
        ██▀███   ▄▄▄▄    █    ██  ██▀███   ██▓    
        ▓██ ▒ ██▒▓█████▄  ██  ▓██▒▓██ ▒ ██▒▓██▒    
        ▓██ ░▄█ ▒▒██▒ ▄██▓██  ▒██░▓██ ░▄█ ▒▒██░    
        ▒██▀▀█▄  ▒██░█▀  ▓▓█  ░██░▒██▀▀█▄  ▒██░    
        ░██▓ ▒██▒░▓█  ▀█▓▒▒█████▓ ░██▓ ▒██▒░██████▒
        ░ ▒▓ ░▒▓░░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░
        ░▒ ░ ▒░▒░▒   ░ ░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░
        ░░   ░  ░    ░  ░░░ ░ ░   ░░   ░   ░ ░   
        ░      ░         ░        ░         ░  ░
                    ░'''+Style.RESET_ALL)

    print(Fore.RED+'''
            ----------------------------
              ► IDN Homograph Attack ◄
                  ► by @rbayuokt ◄
            -----------------------------'''+Style.RESET_ALL)

def howTo():
    print(Fore.YELLOW+'''
    How to use : 
    ● Enter name ( ex : apple )
    ● Enter domain type (ex : .com )
    '''+Style.RESET_ALL)

# convert latin url to Cryrillic character url
# param :
# @nama : name of url ( ex : apple )
# @domain : domain type ( ex : .com )
def attackCryrillic(nama,domain):
    print("\nIDN Homograph Attack with Cryrillic Result :\n")

    # this code is used for check if name of url
    # included a Cryrillic character look alike then 
    # perform attack if there is look alike character
    # if there is not look alike character then give a message
    valid = ['y','a','e','m','h','o','p','c','t','y','x','s','i','j']
    hsl = [valid[i] for i in range(len(valid)) if valid[i] in nama]

    if hsl:
        if 'y' in nama:
            makeUrl('y',nama,CyrillicUnicode[12],'Cyrillic',domain)

        if 'a' in nama:
            makeUrl('a',nama,CyrillicUnicode[11],'Cyrillic',domain)

        if 'e' in nama:
            makeUrl('e',nama,CyrillicUnicode[13],'Cyrillic',domain)

        if 'm' in nama:
            makeUrl('m',nama,CyrillicUnicode[14],'Cyrillic',domain)

        if 'h' in nama:
            makeUrl('h',nama,CyrillicUnicode[15],'Cyrillic',domain)

        if 'o' in nama:
            makeUrl('o',nama,CyrillicUnicode[16],'Cyrillic',domain)

        if 'p' in nama:
            makeUrl('p',nama,CyrillicUnicode[17],'Cyrillic',domain)

        if 'c' in nama:
            makeUrl('c',nama,CyrillicUnicode[18],'Cyrillic',domain)

        if 't' in nama:
            makeUrl('t',nama,CyrillicUnicode[19],'Cyrillic',domain)
            
        if 'y' in nama:
            makeUrl('y',nama,CyrillicUnicode[20],'Cyrillic',domain)

        if 'x' in nama:
            makeUrl('x',nama,CyrillicUnicode[21],'Cyrillic',domain)

        if 's' in nama:
            makeUrl('s',nama,CyrillicUnicode[22],'Cyrillic',domain)

        if 'i' in nama:
            makeUrl('i',nama,CyrillicUnicode[23],'Cyrillic',domain)
            
        if 'j' in nama:
            makeUrl('j',nama,CyrillicUnicode[24],'Cyrillic',domain)
    
    else:
        print(Back.RED+'Sorry... this url not available in Cyrillic :('+Style.RESET_ALL)
        print("\n")


# convert latin url to Greek character url
# param :
# @nama : name of url ( ex : apple )
# @domain : domain type ( ex : .com )
def attackGreek(nama,domain):
    print("\nIDN Homograph Attack with Greek Result :\n")

    # this code is used for check if name of url
    # included a Greek character look alike then 
    # perform attack if there is look alike character
    # if there is not look alike character then give a message
    valid = ['i','k','v','o','u','c','j']
    hsl = [valid[i] for i in range(len(valid)) if valid[i] in nama]

    if hsl:
        if 'i' in nama:
            makeUrl('i',nama,GreekUnicode[15],'Greek',domain)
        
        if 'k' in nama:
            makeUrl('k',nama,GreekUnicode[16],'Greek',domain)

        if 'v' in nama:
            makeUrl('v',nama,GreekUnicode[17],'Greek',domain)

        if 'o' in nama:
            makeUrl('o',nama,GreekUnicode[18],'Greek',domain)

        if 'u' in nama:
            makeUrl('u',nama,GreekUnicode[19],'Greek',domain)

        if 'c' in nama:
            makeUrl('c',nama,GreekUnicode[20],'Greek',domain)

        if 'j' in nama:
            makeUrl('j',nama,GreekUnicode[21],'Greek',domain)
    else:
        print(Back.RED+'Sorry... this url not available in Greek:('+Style.RESET_ALL)
        print("\n")


# this code used for making new url
# with Cyrillic or Greek character included
# so u can perform homograph attack if the url is available
#
# param :
# @char : show match latin look alike character to Cyrillic or Greek
# @nama : name of url 
# @unicode : The order of the Unicode
# @desc : Cyrillic or Greek
# domain : type of domain
def makeUrl(char,nama,unicode,desc,domain):
    namaBaru = nama.replace(char,unicode)
    print(Fore.GREEN+"============================================="+Style.RESET_ALL)
    print("{0}Change the letter {1} with {2} {3} {4}".format(Fore.YELLOW , char , desc , unicode , Style.RESET_ALL) )
    print("{0}► new URL : {1} {2}".format(Fore.GREEN , namaBaru+domain , Style.RESET_ALL ))
    print("{0}► availability : {1} {2}".format(Fore.GREEN , check_domain(namaBaru+domain) , Style.RESET_ALL ))
    print(Fore.GREEN+"=============================================\n"+Style.RESET_ALL)

# show all Cyrillic character
# format : Latin = Cyrillic Character
def showAllCryrillic():
    print("\nFormat :\n"+Back.GREEN+"Latin = Cyrillic Character"+Style.RESET_ALL)
    print("\n")
    for i in range(len(CryrillicList)):
        print("{0} = {1}".format(CryrillicList[i] , CyrillicUnicode[i]))
    
    print("\n")

# show all Greek character
# format : Latin = Greek Character
def showAllGreek():
    print("\nFormat :\n"+Back.GREEN+"Latin = Greek Character"+Style.RESET_ALL)
    for i in range(len(GreekList)):
        print("{0} = {1}".format(GreekList[i] , GreekUnicode[i]))
    
    print("\n")

# this code for back to main menu
def repeat():
    more = input("Again ? (y/n) : ")

    if more.lower() == 'y':
        main()
    elif more.lower() == 'n':
        exit()

def menu():
    print('''
    Main Menu :
    1. IDN Homograph attack with Cryrillic 
    2. IDN Homograph attack with Greek
    3. Show All Cryrillic Character
    4. Show All Greek Character
    5. Exit
    ''')
    pilihan = input("Choose : ")
    
    if pilihan == '1':
        nama = input("\n► Enter name : ")
        domain = input("► Enter domain type : ")
        attackCryrillic(nama.lower(),domain.lower())
        repeat()

    elif pilihan == '2':
        nama = input("\n► Enter a name : ")
        domain = input("► Enter a domain type : ")
        attackGreek(nama.lower(),domain.lower())
        repeat()
    
    elif pilihan == '3':
        showAllCryrillic()
        repeat()
    
    elif pilihan == '4':
        showAllGreek()
        repeat()

    elif pilihan == '5':
        print(Back.GREEN+' Thank you :) '+Style.RESET_ALL)
        sleep(1)
        exit()

    else:
        print(Fore.RED+'Out of range , Try Again...')
        sleep(1)
        main()

def main():
    clear()
    salam()
    howTo()
    menu()

if __name__ == "__main__":
    main()

# please tell me if u found bugs :) 
# thank you