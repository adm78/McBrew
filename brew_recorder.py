#!/usr/bin/python


''' This script is used to record thermal data from the fermenter and
upload it to Dropbox so it may be monitored remotely. For now we are
running with a ficticous stream of temperature data '''

import random
from datetime import datetime
from os.path import expanduser, join

def getTemperature():

    '''return the time. temperature of the fermenter in degC'''

    return (datetime.now()).ctime(), random.uniform(18.0, 23.0)

def recordDataToDB():

    ''' upload the recorded data to Dropbox '''

    #get the Dropbox directory path and open the file
    home = expanduser("~")
    db_path = join(home,'Dropbox','homebrew','brew_recorder')
    rec_filename = join(db_path,'temperature_evolution.txt')
    rec_file = open(rec_filename,'w')
    rec_file.write("#datetime                    temperature/degC \n")
        
    #get/recorder the temperature
    count = 0
    while count < 10:
        current_time, current_temp = getTemperature()
        rec_file.write(current_time + '\t' + str(current_temp) + '\n')
        count = count + 1
    rec_file.close()

def recordMetaDataToDB():
    pass
        
recordDataToDB()
