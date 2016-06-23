#!/usr/bin/python


''' This script is used to record thermal data from the fermenter and
upload it to Dropbox so it may be monitored remotely. For now we are
running with a ficticous stream of temperature data '''

import random
from datetime import datetime
from os.path import expanduser, join
import time
from shutil import copyfile
import os

#global settings:
max_points = 10 #this is the max number of temperature points to store on the Dropbox cache
dt_update = 10 #seconds between updates

def getTemperature():

    '''return the time. temperature of the fermenter in degC'''

    return datetime.now(), random.uniform(18.0, 23.0)

def recordDataToDB(max_points=100,dt_update=dt_update):

    '''upload the recorded data to Dropbox cache. We use two cache
    files. We fill each in sequence. When the second cache fiel is
    full we delete the first and start writing to that. This way we
    retain a short term history and don't have to shift constantly
    delete single lines of the file. A caveat here is that we required
    the reader to know which order to put the data in (this will flip
    everytime) we fill up thw whole cache. Actually it might be better
    to copy over the first fill when the second cache is full. i.e. on
    the first pass we fill cache file, then 2, then copy 2 to 1, fill
    2, copy to 1, fill 2 copy to one. This way we always read the
    cache files as 1 then 2.

    '''

    #get the Dropbox directory path and open the file
    home = expanduser("~")
    db_path = join(home,'Dropbox','homebrew','brew_recorder')
    rec_filenames = [join(db_path,'temperature_evolution_start.txt'),join(db_path,'temperature_evolution_end.txt')]

    #delete the old cache files
    try:
        os.remove(rec_filenames[0])
    except OSError:
        pass
    try:
        os.remove(rec_filenames[1])
    except OSError:
        pass
    
    #initialise the various counters
    first_cache_fill = True
    
    #start the recorder loop
    while True:
        if first_cache_fill:

            # loop over the cache files until both are full
            for i in range(2):
                fillCache(i,max_points,rec_filenames,dt_update)
            first_cache_fill = False
            
        else:
            #both files have previously been filled, copy end cache over start cache
            copyfile(rec_filenames[1], rec_filenames[0])
            fillCache(1,max_points,rec_filenames,dt_update)

def fillCache(cache_index, max_points,rec_filenames,dt_update):

    #writes to a cache file until it's full
    rec_count = 1  #number of temps recorder in the current file
    rec_file = open(rec_filenames[cache_index],'w')
    rec_file.write("#datetime                    temperature/degC \n")
            
    while (rec_count <= max_points):
                
        current_time, current_temp = getTemperature()
        rec_file.write(current_time.isoformat() + '\t' + str(current_temp) + '\n')
        rec_file.flush()
        rec_count = rec_count + 1
        time.sleep(dt_update)
    rec_file.close()
    
def recordMetaDataToDB():
    pass
        
recordDataToDB(max_points=max_points,dt_update=dt_update)
