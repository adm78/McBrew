#!/usr/bin/python

'''This file is part of McBrew. It attempts to read the DBdata generate
by brew_recorder.py and plot the data as it comes in

we weant to file ip an array, with say, 100 points, then we want ot just take the last value and delet the array'''

from os.path import expanduser, join, isfile
from shutil import copyfile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def startReader():

    '''checks the state of the cache and return the data a list of
    filenames'''

    #get the required paths
    home = expanduser("~")
    db_path = join(home,'Dropbox','homebrew','brew_recorder')
    rec_filenames = [join(db_path,'temperature_evolution_start.txt')]
    rec_filenames.append(join(db_path,'temperature_evolution_end.txt'))
    cache_filenames = [join(db_path,'temperature_cache_1.txt')]
    cache_filenames.append(join(db_path,'temperature_cache_2.txt'))


    '''check that the cache files exist'''

    #primary cache check
    if (not isfile(rec_filenames[0])):
        
        print "The primary cache file could not be found! Make sure"
        print "brew_recorder.py is running on the remote machine!"
        sys.exit()

    #secondary cache check
    elif (not isfile(rec_filenames[1])):

        print "Warning: the secondary cache file is not present"
        copyfile(rec_filenames[0],cache_filenames[0])
        pd.read_csv(cache_filenames[0])

    # both cache files are present
    else:
        print "Both cache files have been found!"
        print "Generating temporary caches."
        copyfile(rec_filenames[0],cache_filenames[0])
        copyfile(rec_filenames[1],cache_filenames[1])  
        c0_df = pd.read_csv(cache_filenames[0],sep='\t',dtype={'time': "datetime64[ns]", 'temp': np.float64},names=["time","temp"])
        c1_df = pd.read_csv(cache_filenames[1],sep='\t',dtype={'time': 'datetime64[ns]', 'temp': np.float64},names=["time","temp"])
        print c0_df.index
        print c1_df.index
        
    # #check that the cache files exist
    # for i, rec_file in enumerate(rec_filenames):

    #     #cache I is not present
    #     if (not isfile(rec_file)) and (i==0):
            
    #         print "The primary cache file could not be found! Make sure"
    #         print "brew_recorder.py is running on the remote machine!"
    #         sys.exit()

    #     #cache II is not present
    #     elif (not isfile(rec_file)) and (i==1):
            
    #         print "warning secondary cache file not found"
    #         copyfile(rec_file, cache_file)
    #         df = pd.read_csv(cache_copy, dtype={"CallGuid": np.int64})
            
    #     else:

            
            
    # while count < 1000:
    #     with open(read_filename,'r') as f:
    #         pass
    #     count += 1 
    
startReader()
