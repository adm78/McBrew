#!/usr/bin/python

'''This file is part of McBrew. It attempts to read the DBdata generate
by brew_recorder.py and plot the data as it comes in

we weant to file ip an array, with say, 100 points, then we want ot just take the last value and delet the array'''

from os.path import expanduser, join
from shutil import copyfile
import matplotlib.pyplot as plt

def startReader():

    #get the Dropbox directory path and open the file
    home = expanduser("~")
    db_path = join(home,'Dropbox','homebrew','brew_recorder')
    rec_filename = join(db_path,'temperature_evolution.txt')
    read_filename = join(db_path,'temperature_evolution_read.txt')
    copyfile(rec_filename, read_filename)

    #set up the lists that we're going to plot
    temperature = []
    count = 0
    
    while count < 1000:
        with open(read_filename,'r') as f:
            pass
        count += 1 
            

startReader()
