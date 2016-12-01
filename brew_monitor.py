#!/usr/bin/python

'''This script uploads thermal data from the brew machine to the
plotly server.

Existing issues: If we get kicked out of UniofCam Network then a 
manual sign-in is required...bleugh

'''

import plotly.plotly as py 
import plotly.tools as tls   
import plotly.graph_objs as go
import datetime 
import time
import Adafruit_MCP9808.MCP9808 as MCP9808
import argparse
from socket import error as SocketError

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
parser.add_argument('-p','--points',
                    type=int,default=50,                                                                       
                    help="number of points held on the graph")
args = parser.parse_args() 
time_delay =  args.time_delay*60.0
max_points = args.points

# check that the delay is okay
if time_delay <= 72.0:
    print "Warning: the plotly free Python API limits the user to",
    print "a maximum of 50 API calls per day (one very 72[s]) or 30",
    print "in any hour. The delay between calls can be set using with the,"
    print "-t arg. Current time delay =", time_delay,"[s]."
else:
    print "Updating every", args.time_delay,"[mins]."

#================================================================== 
def send_data(s,sensor):

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = sensor.readTempC()

    # Send data to your plot
    try:
        s.write(dict(x=x, y=y))
    except SocketError:
        print x, ":",
        print "No connection to perfrom write.",
        print "Retrying in", time_delay,"[s]."

#==================================================================    
# intialise the sensor
#==================================================================    

sensor = MCP9808.MCP9808()
sensor.begin()
print "Sensor connection initialised."

#================================================================    
#initialise the plotly stream
#================================================================    

stream_ids = tls.get_credentials_file()['stream_ids']
#print stream_ids

# Get stream id from stream id list 
stream_id = stream_ids[0]

# Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=max_points # keep a max of max_points pts on screen
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
layout = go.Layout(title='Lagering Chamber',
                   xaxis=dict(title="Time"),
                   yaxis=dict(title="Temperature/degC"))

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.plot(fig, filename='Oktoberfest_stream',auto_open=False)


#start of continuous streaming section
# We will provide the stream link object the same token that's 
# associated with the trace we wish to stream to
s = py.Stream(stream_id)

#================================================================= 
# begin streaming
#=================================================================   
# We then open a connection
s.open()

count = time_delay
first_pass_log = True

# stream the data, heartbeating every 30[s]
while True:
    
   #check if data point needs to be streamed
   if count >= time_delay:
       send_data(s,sensor)
       count = 0
       if first_pass_log:
           print "Streaming initiated at",
           print "https://plot.ly/~adm78/3/lagering-chamber/"
           first_pass_log = False

   # #send a heartbeat, handling socket error    
   try:
       s.heartbeat()
   except SocketError:
       print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), ":",
       print "No connection to perform heartbeat.",
       print "Retrying in 30[s]."
   
   time.sleep(30)
   count += 30
 
# Close the stream when done plotting
s.close()








