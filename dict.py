from __future__ import print_function
import json
import os
import random
from colorama import init
from termcolor import colored
from difflib import get_close_matches

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


def close_word():
 if len(get_close_matches(x, file2.keys())) > 0 :
   similar_list = get_close_matches(x,file2.keys())
   a = random.choice(similar_list)
   close = raw_input("\nDid you mean %s instead? Enter Y if yes, or N if no: " %(a) )
   if close == 'y' or close == 'yes':
        print(colored("\n"+ file2[a] , 'white' , "on_blue"))
   elif close == 'n' or close == 'no':
        what = raw_input(colored("\nDo you want to add the meaning of this word (Y,N) :",'grey','on_green')).lower()
        append_data(what)

def hello():
    clear()
    print(colored("============================",'white'))
    print(colored('\nWellcome to Dictionary V1.0 ^_^ \n','white'))
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
        print(colored("\nThanks for use it  :)",'grey','on_green'))


def english_dict():
    global x
    x = raw_input(colored("\nplease tell me what's the word that you look up : ","cyan")).lower()
    try:
        print(colored("\n"+str(file2[x]) , 'white' , "on_blue"))
        restart()
    except:
        try:
            if type(file[x]) == list :
                for word in file[x] :
                    print(colored("\n"+ word , 'white' , "on_blue"))
                    restart()
            else:
                    print(colored("\n"+str(file[x]) , 'white' , "on_blue"))
                    restart()
        except:
           clear()
           print(colored("\nthis word ain't available :(",'white','on_red'))
           close_word()
           restart()

init()

try:
    clear()
    hello()
    english_dict()
except KeyboardInterrupt:
        print(colored("\nThanks for use it  :)",'grey','on_green'))
