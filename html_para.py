#! /usr/tmp/env python3
# Guns up, lets do this leeroy. 
# LeeroyJenkins, circa 2005

import os
import sys
import datetime

def getParagraph(selection):
    switcher = {
        1: para1,
        2: para2,
        3: para3,
        4: para4,
        5: para5,
        6: para6,
        7: para7,
        8: para8,
        9: para9,
    }
    return switcher.get(selection)

os.system('clear')
continue_loop = 'Y'
runner = 0
access_time = datetime.datetime.now() # prints current date time to the variable access_time
user = os.getlogin() # stores username to the varibale users

intro = '''
    WelCoMe!!!!!!!!!!!!! 
    usage, Y or N to quit, or CTRL+C
    hours of enjoyment.

'''
print(intro, end ='?.>\n\t')

para1='''[!] THE ORIGINATOR 1's are originals. Coming up with new ideas
and executing them is natural. Having things their own way is another
trait that gets them as being stubborn and arrogant. 1's are extremely
honest and do well to learn some diplomacy skills. They like to take
the initiative and are often leaders or bosses, as they like to be the
best. Being self-employed is definitely helpful for them. Lesson to
learn: Others' ideas might be just as good or better and to stay open
minded. Famous 1's: Tom Hanks, Robert Redford, Hulk Hogan, Carol
Burnett, Wynona Judd, Nancy Reagan, Raque l Welch.[!]  '''

para2='''[!] THE PEACEMAKER 2's are the born diplomats. They are aware of
others' needs and moods and often think of others before themselves.
Naturally analytical and very intuitive they don't like to be alone.
Friendship and companionship is very important and can lead them to be
successful in life, but on the other hand they'd rather be alone than
in an uncomfortable relationship. Being naturally shy they should
learn to boost their self-esteem and express themselves freely and
seize the moment and not put things off. Famous 2's: President Bill
Clinton, Madonna, Whoopee Goldberg, Thomas Edison, Wolfgang Amadeus
Mozart.[!]  '''

para3='''[!] THE LIFE OF THE PARTY 3's are idealists. They are very
creative, social, charming, romantic, and easygoing. They start many
things, but don't always see them through. They like others to be
happy and go to great lengths to achieve it. They are very popular and
idealistic. They should learn to see the world from a more realistic
point of view.  Famous 3's: Alan Alder, Ann Landers, Bill Cosby,
Melanie Griffith, Salvador Dali, Jodi Foster.[!] '''

para4='''[!]THE CONSERVATIVE 4's are sensible and traditional. They like
order and routine. They only act when they fully understand what they
are expected to do. They like getting their hands dirty and working
hard. They are attracted to the outdoors and feel an affinity with
nature. They are prepared to wait and can be stubborn and persistent.
They should learn to be more flexible and to be nice to themselves.
Famous 4's: Neil Diamond, Margaret Thatcher, Arnold Schwarzenegger,
Tina Turner, Paul Hogan, Oprah Winfrey. [!] '''

para5='''[!] THE NONCONFORMIST 5's are the explorers. Their natural
curiosity, risk taking, and enthusiasm often land them in hot water.
They need diversity, and don't like to be stuck in a rut. The whole
world is their school and they see a learning possibility in every
situation. The questions never stop.  They are well advised to look
before they take action and make sure they have all the facts before
jumping to conclusions.  Famous 5's: Abraham Lincoln, Charlotte
Bronte, Jessica Walter, Vincent Van Gogh, Bette Midler, Helen Keller
and Mark Hail.[!]  '''

para6='''[!] THE ROMANTIC 6's are idealistic and need to feel useful to be
happy.  A strong family connection is important to them. Their actions
influence their decisions. They have a strong urge to take care of
others and to help.  They are very loyal and make great teachers. They
like art or music.  They make loyal friends who take the friendship
seriously. 6's should learn to differentiate between what they can
change and what they cannot.  Famous 6's: Albert Einstein, Jane
Seymour, John Denver, Meryl Streep, Christopher Columbus, Goldie Hawn. [!]
'''

para7='''[!] THE INTELLECTUAL 7's are the searchers. Always probing for
hidden information, they find it difficult to accept things at face
value. Emotions don't sway their decisions. Questioning everything in
life, they don't like to be questioned themselves. They're never off
to a fast start, and their motto is slow and steady wins the race.
They come across as philosophers and being very knowledgeable, and
sometimes as loners. They are technically inclined and make great
researchers uncovering information.  They like secrets. They live in
their own world and should learn what is acceptable and what is not in
the world at large.  Famous 7's: William Shakespeare, Lucille Ball,
Michael Jackson, Joan Baez, Princess Diana. [!]'''

para8='''[!] THE BIG SHOT 8's are the problem solvers. They are
professional, blunt and to the point, have good judgment and are
decisive. They have grand plans and like to live the good life. They
take charge of people They viewpeople objectively. They let you know
in no uncertain terms that they are the boss! They should learn to
exude their decisions on their own needs rather than on what others
want.  Famous 8's: Edgar Cayce, Barbara Streisand, George Harrison,
Jane Fonda, Pablo Picasso, Aretha Franklin, Nostrodamus. [!]'''

para9='''[!] THE PERFORMER 9's are natural entertainers. They are very
caring and generous, giving away their last dollar to help. With their
charm, they have no problem making friends and nobody is a stranger to
them. They have so many different personalities that people around
them have a hard time understanding them. They are like chameleons,
ever changing and blending in. They have tremendous luck, but also can
suffer from extremes in fortune and mood. To be successful, they need
to build a loving foundation.  Famous 9's: Albert Schweitzer, Shirley
MacLaine, Harrison Ford, Jimmy Carter, Elvis Presley. [!]'''

while continue_loop == 'Y':
    accum1 = 0
    accum2 = 0
    accum3 = 0
    accum4 = 0
    header = '<!DOCTYPE html>\n<html>\n<body>' # prepared html tags
    footer = '</body>\n</html>' # prepared closing html tags
    os.chdir('~/public_html/') # ensure it is accessible from our web-root dir.
    name = input("What is your name friend?\n").lower() # keep it lower case for ease of use on cmd-line
    generated_File = name + '.html' # store users name + html extension.
    file_Holder = open(generated_File, 'wt') # open as write-text mode to ensure no 2 files exist with the same name.
    log_File = open('~/logs/rotating_birth_log.csv', 'at') # append to log file. keep a rolling log.
    try:
        bday = int(input("Please enter the day you were born! \n->"))
        bmonth = int(input("Please enter the month you were born\n ->"))
        byear = int(input("Please enter the year you were born!\n->"))
        birth = bday + bmonth + byear
        sum1 = str(birth)
        for x in sum1:
            accum1 += int(x)
            accum2 = str(accum1)
        accum3 = int(accum2[0]) + int(accum2[1])
        if accum3 > 9:
            accum3 = str(accum3)
            for x in str(accum3):
                accum4 += int(x)
            data = [header, str(name), ' >> ', str(accum4),' >> \n',str(getParagraph(accum4)), footer] # creates a managable data set.
            file_Holder.write(''.join(data)) # writes HTML and user data into file.
            file_Holder.close()
            runner +=1 # incriment the counter.
            access = ['PROGRAM RAN AT: ',str(access_time),'\n RUNNING COUNTER: ',str(runner), ' RAN BY:', user, '\n']
            log_File.write(''.join(access)) # appends to log file. with date/time and username.
            print("Your Birth paragraph is located within this file:",name,".html!!") # alerts the user as to where the file is store.
            #TODO, get the absolute path to the stored html file.
        elif int((accum3 >= 1)) or int((accum3 <= 9)):
                runner +=1
                access2 = ['PROGRAM RAN AT: ',str(access_time),'\n RUNNING COUNTER: ',str(runner), ' RAN BY:', user, '\n']
                log_File.write(''.join(access2)) # appends to log file with second data set.
                log_File.close()
                data = [header, str(name), ' >> ', str(accum3),' >>\n ',str(getParagraph(accum3)), footer] # generates second dataset
                file_Holder.write(''.join(data)) # writes second data set.
                file_Holder.close()
                print("Your Birth paragraph is located within this file:",name,".html!!")
     except ValueError:
        os.system('clear')
        print("[+] Sorry, i didn't quite get that... \n")
        continue_loop = input("[+] Would you like to try again? Y or N\n->\t").upper()
