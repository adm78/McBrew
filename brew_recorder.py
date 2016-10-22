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
                 " For now we are running with ficticous thermal data." +
                 " Uses dropbox_uploader to upadte the remote cache for " +
                 " Raspian compatiblity."),                                                            
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
parser.add_argument('-d','--debug', 
                    default=False, action="store_true",                                                                                     
                    help=("the verbose option."))


args = parser.parse_args() 
max_points =  args.max
dt_update = args.dt
dt_terminate = args.end
debug_log = args.debug


#==================================================================                                                      
# various function definitions                                                                                                      
#==================================================================  
def get_temperature():

    '''return the time. temperature of the fermenter in degC'''
    return datetime.now(), random.uniform(18.0, 23.0)


def init_recorder(max_points=100,dt_update=dt_update):

    ''' this is the main data collection loop '''

    #define the cache files
    local_cache = ['T_cache_1.csv', 'T_cache_2.csv']

    #delete the old cache files
    for i in range(2):
        try:
            os.remove(local_cache[i])
        except OSError:
            pass
        delete_remote_cache(local_cache[i])
 
    #initialise the various counters
    first_cache_fill = True
    
    #start the recorder loop
    while True:
        if first_cache_fill:

            # loop over the cache files until both are full
            for i in range(2):
                fill_cache(i,max_points,local_cache,dt_update)
            first_cache_fill = False
            
        else:
            #both files have previously been filled, copy end cache over start cache
            copyfile(local_cache[1], local_cache[0])
            update_remote_cache(local_cache[0])
            fill_cache(1,max_points,local_cache,dt_update)


def fill_cache(cache_index, max_points,local_cache,dt_update):

    #writes to a cache file until it's full
    rec_count = 1  #number of temps recorder in the current file
    active_cache = open(local_cache[cache_index],'w')
    # active_cache.write("#date" + 2*'\t' + "time" 
    #                    + 2*'\t' + "temperature/degC" + "\n")
            
    while (rec_count <= max_points):
                
        current_time, current_temp = get_temperature()
        active_cache.write(current_time.strftime("%d/%m/%Y %H:%M:%S") + 
                           ';' + str(current_temp) + '\n')
        active_cache.flush() #forces the local cache to update
        update_remote_cache(local_cache[cache_index])
        rec_count = rec_count + 1
        time.sleep(dt_update)
    active_cache.close()

def update_remote_cache(cache_filename):
    
    if debug_log:
        options = ""
    else: 
        options = "-q "
    update_cmd = ("dropbox_uploader.sh " + options + "upload " + cache_filename +
           " " + cache_filename)
    os.system(update_cmd)

def delete_remote_cache(cache_filename):
     
    if debug_log:
        options = ""
    else: 
        options = "-q "
    delete_cmd = ("dropbox_uploader.sh " + options + "delete " + cache_filename)
    os.system(delete_cmd)
     
init_recorder(max_points,dt_update)
