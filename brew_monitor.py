#!/usr/bin/python

'''This script uploads thermal data from the brew machine to the
plotly server.
Note: currently generating random thermal data'''

import numpy as np 
import plotly.plotly as py 
import plotly.tools as tls   
import plotly.graph_objs as go
import datetime 
import time
import random
import Adafruit_MCP9808.MCP9808 as MCP9808
import argparse

#==================================================================                                                      
# command line args                                                                                                      
#==================================================================                                                      
parser = argparse.ArgumentParser(                                                                                        
    description=("reads data from MCP9808 temperature sensor" +
                 "via i2c and streams live to plotly server" +
                 "at https://plot.ly/~adm78/0/primary-fermenter-test/"),                                                            
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)                                                              
parser.add_argument('-t','--time_delay',
                    type=float,default=5.0,                                                                                     
                    help="time delay between updates in [mins]")

args = parser.parse_args() 
time_delay =  args.time_delay*60.0
print "Updating every", args.time_delay,"[mins]"

#==================================================================    
# intialise the sensor
#==================================================================    

sensor = MCP9808.MCP9808()
sensor.begin()

#==================================================================    
#initialise the plotly stream
#==================================================================    

stream_ids = tls.get_credentials_file()['stream_ids']
print stream_ids

# Get stream id from stream id list 
stream_id = stream_ids[0]

# # Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=36      # keep a max of 80 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Primary Fermenter Test',
                   xaxis=dict(title="Time"),
                   yaxis=dict(title="Temperature/degC"))

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.plot(fig, filename='python-streaming')



#start of continuous streaming section
# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

#==================================================================    
# begin streaming
#==================================================================
    
# We then open a connection
s.open()

i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5) 

while True:
    
    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = sensor.readTempC()

    # Send data to your plot
    s.write(dict(x=x, y=y))
    
    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
            
    time.sleep(time_delay)  # plot a point every second    
# Close the stream when done plotting
s.close()





