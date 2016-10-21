#!/usr/bin/python

import random
from datetime import datetime
from os.path import expanduser, join
import time
from shutil import copyfile
import os
import argparse 

#==================================================================                                                      
# command line args                                                                                                      
#==================================================================                                                      
parser = argparse.ArgumentParser(                                                                                        
    description=("Updates a cache (Dropbox) with the latest" +
                 " thermal data from the brew machine." +
                  " For now we are running with ficticous thermal data."),                                                            
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)                                                              

parser.add_argument('-m','--max',
                    type=int,default=10,                                                                                     
                    help="the number of data-points to keep in the cache history")
parser.add_argument('-t','--dt', 
                    type=float,default=2.0,                                                                                     
                    help="the number of seconds between consecutive thermal readings")  
parser.add_argument('-e','--end', 
                    type=float,default=-1,                                                                                     
                    help=("the time (hrs) to elapse before this script" + 
                          "auto-terminates, -1=infinite"))

args = parser.parse_args() 
max_points =  args.max
dt_update = args.dt
dt_terminate = args.end


#==================================================================                                                      
# various function definitions                                                                                                      
#==================================================================  
def getTemperature():

    '''return the time. temperature of the fermenter in degC'''
    return datetime.now(), random.uniform(18.0, 23.0)


def recordDataToDB(max_points=100,dt_update=dt_update):

    ''' this is the main data collection loop '''

    #get the Dropbox directory path and open the file
    home = expanduser("~")
    db_path = join(home,'Dropbox','homebrew','brew_recorder')
    rec_filenames = [join(db_path,'T_cache_1.txt'),join(db_path,'T_cache_2.txt')]

    #delete the old cache files
    for i in range(2):
        try:
            os.remove(rec_filenames[i])
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
    rec_file.write("#date" + 2*'\t' + "time" + 2*'\t' + "temperature/degC" + "\n")
            
    while (rec_count <= max_points):
                
        current_time, current_temp = getTemperature()
        rec_file.write(current_time.strftime("%d/%m/%Y\t%H:%M:%S") + '\t' + str(current_temp) + '\n')
        rec_file.flush()
        rec_count = rec_count + 1
        time.sleep(dt_update)
    rec_file.close()
    
     
recordDataToDB(max_points=max_points,dt_update=dt_update)
