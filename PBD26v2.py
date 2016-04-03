#title           :PBD-26
#description     :With the 15 items in the python dictionary remove a key from one of the results.
#author          :MC
#date            :03/04/2016
#version         :0.2
#notes           :
#python_version  :3.5.1
 #!/usr/bin/python

import os
import time

clear = lambda : os.system('cls')

countriesOfTheWorld = {
    'Afghanistan': 'AFG',
    'Aland Islands': 'ALA',
    'Albania': 'ALB',
    'Algeria': 'DZA',
    'American Samoa': 'ASM',
    'Andorra': 'AND',
    'Angola': 'AGO',
    'Anguilla': 'AIA',
    'Antarctica': 'ATA',
    'Antigua and Barbuda': 'ATG',
    'Argentina': 'ARG',
    'Armenia': 'ARM',
    'Aruba': 'ABW',
    'Australia': 'AUS',
    'Austria': 'AUT',
    'Azerbaijan': 'AZE'}

k2del = input('Please enter the key you wish to delete: ')

if k2del in countriesOfTheWorld:
    userDelYN = input("Please confirm you wish to delete: %s by pressing 'Y'"
              % k2del)
    if userDelYN == 'Y' or userDelYN == 'y':
        del countriesOfTheWorld[k2del]
        print ('SUCCESS: The key %s has been successfully deleted.' % k2del)
        time.sleep(2)
elif userDelYN == 'N' or userDelYN == 'n':
    print ("The key '%s'  has the value '%s' and has not been deleted." % (k2del, countriesOfTheWorld[k2del]))
    time.sleep(2)
else:
    print ('ERROR: THE VALUE YOU ENTERED DOES NOT EXIST IN DICTIONARY')
    time.sleep(2)

endOfScript = input(' ')

            