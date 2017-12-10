#! /usr/bin/env python3
# Turtle gui with chinese paragraphs
# oldkingcone_lab11
# oldkingcone
# guns up lets do this.

try:
    #from selenium import webdriver
    import sqlite3
    from pathlib import Path
    import webbrowser
    import matplotlib as mpl
    import shutil
    from shutil import copy
    import configparser
    import os
    #import psycopg2  # INSTALL PSYCOPG2!!!!!!!
    import turtle
    from time import sleep
    import datetime
    import tkinter as tk

    import chyr
    import para
except (ImportError, ImportWarning) as whoops:
    logfile = open('gui_use_log.log','at')
    inerror = {'\nSorry, the selected package did not import correctly or does not exist on this system, please...' \
          'consider running sudo -H pip3 install, this/these modules: ', str(whoops), '\n'}
    logfile.write(''.join(inerror))
    pass
try:
    # constants that will be reused.
    try:
        workingDir = Path('oldkingcone_lab11.py').absolute()
        browser = Path('firefox.exe').resolve().absolute()
    except (FileNotFoundError):
        pass
    current_year = datetime.date.today().year
    access_time = datetime.datetime.now()
    winn=0
    screen = turtle.Screen()
    screen.setup(1000,1000)
    screen.bgpic('under_the_clouds.png')

    # html file generation
    header = '<!DOCTYPE html>\n<html>\n'
    cssInsert = '<head>\n<link rel=\"stylesheet\" href=\"base.css\">'
    gglTextInsert = '\n<link href=\"https://fonts.googleapis.com/css?family=Aclonica\" rel=\"stylesheet\">\n</head>\n<body>'
    footer = '\n</body>\n</html>'
    usrname = turtle.textinput("Name", "What is your name?")
    htmlFile = usrname + '.html'
    generatedFile = open(htmlFile, 'wt')
    # getting PATH and setting perm directory to use for temp stuff.
    # boom, cross platform, and a rotating log.
    try:
        if os.confstr('CS_PATH') != OSError or os.confstr('CS_PATH') != ValueError:
            # the os.confstr is only avail on linux/unix systems. SO! this will always be true
            # so long as the system is a unix based system! clever little work around imo.
            try:
                linux = os.mkdir('./gui_logs/')
                if linux != OSError or linux != PermissionError:
                    os.chdir('./gui_logs/')
                    logfile = open('gui_use_log.log', 'a')
                    logfile.write('\nUnix based systems have been selected!\n')
                    linUX = './gui_logs/'

            except FileExistsError as err:
                logfile = open('gui_use_log.log', 'a')
                defo = {' \nSelected Unix based system and file already exists, continuing.', str(err), '\n'}
                logfile.write(''.join(defo))
                pass
                try:
                    shutil.copy('./base.css', './gui_logs/')
                    shutil.copy('deadpoool.jpg', './gui_logs/')
                    logfile.write('Copied the 2 required files for the CSS to work!!')
                except (PermissionError) as why:
                    logfile.open('gui_use_log.log', 'a')
                    expl = {' \nSadly... I could not copy the files over, skipping. ', str(why), '\n'}
                    logfile.write(''.join(expl))
                    pass
                access = ['PROGRAM RAN AT: ', str(access_time), ' RAN BY: ', usrname, '\n\n']
                logfile.write(''.join(access))
                logfile.close()
            pass
    except (OSError, AttributeError, IOError, ValueError) as e:
        pass
        # covering my bases here with this, it will raise a ValueError on windows because the os.confstr does not exist.
        # but need to handle none the less, and still establish the areas we want.
        try:
            winner = os.mkdir('./public_html')
            os.chdir('./public_html')
            winder = './public_html'
            winn = 1
            # driver = webdriver.Chrome()
            logfile = open('gui_use_log.log', 'at')
            logfile.write('\nWindows has been Selected!!!\n')
        except FileExistsError as type:
            logfile = open('gui_use_log.log', 'a')
            reas = {'\nFile exists: ', str(type), 'continuing! \n'}
            logfile.write(''.join(reas))
            pass
            try:
                shutil.copy('./base.css', './public_html')
                shutil.copy('./deadpool.jpg', './public_html')
                logfile = open('gui_use_log.log', 'a')
                logfile.write('\nTransfered 2 files successfully!\n')
            except (PermissionError, FileExistsError, FileNotFoundError) as writeerror:
                logfile = open('gui_use_log.log', 'a')
                wild = {'\n Write error happened: ', str(writeerror), '\n'}
                logfile.write(''.join(wild))
                pass
            access = ['\nPROGRAM RAN AT: ', str(access_time), ' RAN BY: ', usrname, '\n']
            logfile.write(''.join(access))
            logfile.close()
        pass

    # get user numbers
    year = turtle.numinput("Birth Year", "Enter the year you were born!", 1990, minval=1900, maxval=2017)
    month = turtle.numinput("Birth Month", "Enter the digit Month you were born!", 1, minval=1, maxval=12)
    day = turtle.numinput("Birth Day", "Enter the Digit day you were born!", 1, minval=1, maxval=31)
    logfile = open('gui_use_log.log', 'a')
    logfile.write(' \nCollected year, month, and day from the user!\n')
    logfile.close()

    # selection of chinese birth year.
    chbyr1 = int(year - 1899) % 12
    if chbyr1 == 0: chbyr1 = 12
    chbyr2 = chyr.getChyr(chbyr1)

    # selection of numerology paragraph.
    bpara = int(day + month + year) % 9
    if bpara == 0: bpara = 9
    bpara2 = para.getParagraph(bpara)

    # biorythm logic?
    biorythm = (((month + year - current_year) * 365) % 30) * .01
    logfile = open('gui_use_log.log', 'a')
    logfile.write(' \nSuccessfully calculated all given number sets.\n')
    logfile.close()

    conn = sqlite3.connect('namesdates.sqlite')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS namesdates(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  datestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, name TEXT, dob TEXT, zodiac TEXT)""")
    sql_stmt = "INSERT INTO namesdates(name, dob, zodiac) VALUES ('%s','%s', '%s')"
    sqlstmt2 = str(sql_stmt)
    c.execute(sqlstmt2 % (str(usrname), str(chbyr1) , str(bpara)))
    conn.commit()
    # gui magic begins here.
    data = [header, cssInsert, gglTextInsert, '\n', '<div class="table chyr">', str(usrname), ' >> ', str(chbyr2),
            '</div>', '\n',
            '<div class="table numor">', str(bpara2), '\n</div>', '\n', footer]
    generatedFile.write(''.join(data))

    logfile = open('gui_use_log.log', 'a')
    logfile.write('\nSuccessfully generated HTML file!\n')
    logfile.close()

    # build a line to display to the user
    line1 = ("Hello " + usrname + " your sum is \n" + str(bpara) + '\n' + chbyr2)
    line2 = ("Numerology:\n" + bpara2)

    # display results
    logfile = open('gui_use_log.log', 'a')
    logfile.write(' \nProgram ran successfully, Terminating gracefully!\n\n')
    logfile.close()
    turtle.write(line1, False, align="center", font=('Arial', 10, 'bold'))
    sleep(10)
    turtle.clear()
    turtle.write(line2, False, align="center", font=('Arial', 10, 'underline'))
    sleep(10)
    turtle.clear()


except (KeyboardInterrupt, TypeError):
    logfile = open('gui_use_log.log', 'a')
    logfile.write('\nCTRL+C was pressed, or the user did not put any data in to the fields. Exiting.')
    logfile.close()
    screen.setup(1000,1000)
    screen.bgcolor('orange')
    screen.bgpic("./cryingdoge.png")
    lineOuch = (
    'So sad to see you leave.. no love for me i see, not even with all the pretty pictures that i drew for you. '
    'Good-bye!')
    turtle.write(lineOuch, False, align="center", font=('Arial', 12, 'bold'))
    sleep(15)
    turtle.clear()
    pass
