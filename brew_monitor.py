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

def get_temperature():

    '''return the time. temperature of the fermenter in degC'''
    return random.uniform(18.0, 23.0)

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

# We then open a connection
s.open()

i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5) 

while True:
    
    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = get_temperature()

    # Send data to your plot
    s.write(dict(x=x, y=y))
    
    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
            
    time.sleep(300)  # plot a point every second    
# Close the stream when done plotting
s.close()





