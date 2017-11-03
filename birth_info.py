#! /usr/bin/env python3
# lab04_paraprinting.py
# oldkingcone
# Guns up, lets do this leeroy.
# LeeroyJenkins, circa 2005

import datetime
import os
import webbrowser

from para import paragraphs

os.system('clear')
continue_loop = 'Y'
access_time = datetime.datetime.now()
user = os.getlogin()

intro = '''
    WelCoMe!!!!!!!!!!!!! 
    usage, Y or N to quit, or CTRL+C
    hours of enjoyment.

'''
print(intro, end='?.>\n')
while continue_loop == 'Y':
    accum1 = 0
    accum2 = 0
    accum3 = 0
    accum4 = 0
    hdr = '<!DOCTYPE html>\n<html>\n<body>'
    ftr = '</body>\n</html>'
    os.chdir('~/public_html/')
    name = input("What is your name friend?\n").lower()
    lgf = name+'.html'
    lef = open(lgf,'wt')
    lof = open('~/logs/rotating_birth_log.csv', 'at')
    try:
        bday = int(input("Please enter the day you were born! \n->"))
        bmonth = int(input("Please enter the month you were born\n ->"))
        byear = int(input("Please enter the year you were born!\n->"))
        birth = bday + bmonth + byear
        sum1 = str(birth)
        for x in sum1:
            accum1 += int(x)
            accum2=str(accum1)
        accum3 = int(accum2[0])+int(accum2[1])
        if accum3 > 9:
            accum3 = str(accum3)
            for x in str(accum3):
                accum4 += int(x)
            stuff = paragraphs.getParagraph(accum4)
            data = [hdr, '\n', str(name), ' >> ', str(accum4), ' >> \n', stuff, '\n', ftr]
            lef.write(''.join(data))
            lef.close()
            runner = 0
            runner = runner+1
            access = ['PROGRAM RAN AT: ', str(access_time), '\n RUNNING COUNTER: ', ' RAN BY: ', user, '\n']
            lof.write(''.join(access))
            print("Your Birth paragraph is located within this file:", name, ".html!!")
            browser_Tab1 = 'http:////localhost/'+lgf # will not load properly.
            webbrowser.open(str(browser_Tab1))
        elif int((accum3 >= 1)) or int((accum3 <= 9)):
                runner = 0
                runner = runner+1
                access2 = ['PROGRAM RAN AT: ', str(access_time), '\n RUNNING COUNTER: ', ' RAN BY: ', user, '\n']
                lof.write(''.join(access2))
                lof.close()
                stuff2 = paragraphs.getParagraph(accum3)
                data = [hdr, '\n', str(name), ' >> ', ' >>\n ', stuff2, '\n', ftr]
                lef.write(''.join(data))
                lef.close()
                print("Your Birth paragraph is located within this file:", name, ".html!!")
                browser_Tab2='http:////localhost/'+lgf #will not load properly.
                webbrowser.open(str(browser_Tab2))
    except (ValueError, OSError, TypeError, RuntimeError, KeyboardInterrupt) as error:
        excp = ["\nError encountered: ", str(error), '\n', "From User: ", str(user), " Date: ", str(access_time)]
        lof.write(''.join(excp))
        lof.close()
        os.system('clear')
        print("[+] Sorry, i didn't quite get that... \n")
        continue_loop = input("[+] Would you like to try again? Y or N\n->").upper()
