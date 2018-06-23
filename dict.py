from __future__ import print_function
import json
import os
from colorama import init
from termcolor import colored

file = json.load(open("data.json"))
file2 = json.load(open("dictionary.json"))
x = ''

def append_data(what):
   if what == "y":

      name = x
      value = raw_input("\ngive the meaning of this word : ")
      with open('data.json') as json_file:
         json_decoded = json.load(json_file)

      json_decoded[name] = value

      with open('data.json', 'w') as json_file:
        json.dump(json_decoded, json_file)
   else:
       restart()



def hello():
    clear()
    print(colored("============================",'white'))
    print(colored('Wellcome to Dictionary V1.0 ^_^ \n','white'))
    print(colored("Thank WebstersEnglishDictionary for data.json ^_^ \n",'white'))
    print(colored("============================",'white'))


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
       os.system('clear')

def restart():
    restart = raw_input(colored("\nDo you want to look up another word (Y,N) : ","green")).lower()
    if restart == 'y' :
        english_dict()
    else:
        print(colored("Thanks for use it  :)",'white','on_green'))


def english_dict():
    global x
    x = raw_input(colored("\nplease tell me what's the word that you look up : ","cyan")).lower()
    try:
        print(colored("\n"+str(file2[x]) , 'white' , "on_blue"))
        restart()
    except:
        try:
            print(colored("\n"+str(file[x]) , 'white' , "on_blue"))
            restart()
        except:
           clear()
           print(colored("\nthis word ain't available :(",'white','on_red'))
           what = raw_input(colored("\nDo you want to add the meaning of this word (Y,N) :",'grey','on_green')).lower()
           append_data(what)
           restart()

init()
clear()
try:
    hello()
    english_dict()
except KeyboardInterrupt:
        print(colored("Thanks for use it  :)",'white','on_green'))
