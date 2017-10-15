#!/usr/bin/python

'''
This script uploads thermal data from the brew machine to the plotly
server. 
'''
#==================================================================
# User defined set-up parameters
#==================================================================
# local_logfile variable is used to define path to where the local
# logfile should be created. Only progress/debug info is written to this
# file (i.e. no thermal time-series data).
local_logfile = '/home/pi/bm.log'

# dropbox_uploader should indicate the full path to the
# dropbox_uploader.sh used to upload to the local logfile.
# This is an optional feature.
# If you don't want to use this feature then set
# dropbox_uploader = ''.
dropbox_uploader = '/home/pi/software/dropbox_uploader/dropbox_uploader.sh'

# remote_url should indicate where the trace is being streamed to.
# This variable just affects what's written to the log files.
remote_url = 'https://plot.ly/~adm78/0/primary-fermenter-test/'

#==================================================================

# ==================================================================                                                      
# module imports                                                                                                     
# ==================================================================
logfile = open(local_logfile,'a')
logfile.write("brew_monitor.py: hello world. Starting module imports...\n")
logfile.flush()

import plotly.plotly as py 
import plotly.tools as tls   
import plotly.graph_objs as go
import datetime 
import time
import Adafruit_MCP9808.MCP9808 as MCP9808
import argparse
from socket import error as SocketError
import os
import subprocess


logfile.write("brew_monitor.py: I've just imported all the modules.\n")
logfile.flush()
# ==================================================================                                                      
# command line args                                                                                                      
# ==================================================================             

parser = argparse.ArgumentParser(                                                                                        
    description=("reads data from MCP9808 temperature sensor" +
                 "via i2c and streams live to plotly server" +
                 remote_url),                                                            
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)                                                              
parser.add_argument('-t','--time_delay',
                    type=float,default=30.0,                                                                                     
                    help="time delay between updates in [mins]")
parser.add_argument('-p','--points',
                    type=int,default=200,                                                                       
                    help="number of points held on the graph")
args = parser.parse_args() 
time_delay =  args.time_delay*60.0
max_points = args.points

logfile.write("brewing_monitor.py: I've just parse the args. ")
logfile.write("About to check time delay\n")

# check that the delay is okay
if time_delay <= 1680.0:
    logfile.write("------------------------------------------------------------\n")
    logfile.write("Warning: the plotly free Python API limits the user to")
    logfile.write("a maximum of 50 API calls per day (one very ~28[mins]) or 30")
    logfile.write("in any hour. The delay between calls can be set using the")
    logfile.write("-t arg. Current time delay = "+ str(time_delay) + "[s].\n")
    logfile.write("------------------------------------------------------------\n")
else:
    logfile.write("Updating every" +  str(args.time_delay) + "[mins].\n")
logfile.flush()    

#check to see if the dropbox uploader script exists
upload_log = False
if dropbox_uploader != '':
    if os.path.isfile(dropbox_uploader):
        upload_log = True

logfile.write("brewing_monitor.py: I've just check the time delay. ")
logfile.write("About to start the sensor connection")
logfile.flush()
#================================================================== 
def send_data(s,sensor):

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = sensor.readTempC()

    # Send data to your plot
    try:
        s.write(dict(x=x, y=y))
    except SocketError:
        logfile.write(str(x) + " :\n")
        logfile.write("No connection to perfrom write.",)
        logfile.write("Retrying in " + str(time_delay) + "[s].\n")
        logfile.flush()
#==================================================================    
# intialise the sensor
#==================================================================    

sensor = MCP9808.MCP9808()
sensor.begin()
logfile.write("Sensor connection initialised.\n")
logfile.write("brew_monitor.py: About to rey and get the stream ids\n")
logfile.flush()
#================================================================    
# initialise the plotly stream
#================================================================    

# Get stream id from stream id list 
stream_ids = tls.get_credentials_file()['stream_ids']
stream_id = stream_ids[0]

logfile.write("brew_monitor.py: got the stream ids. About to start go.Stream...\n")
logfile.flush()

# Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=max_points # keep a max of max_points pts on screen
)

logfile.write("brew_monitor.py: stream_1 object created.")
logfile.write("About to try an initialise the trace...\n")
logfile.flush()

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

logfile.write("brew_monitor.py: go.Data completed.")
logfile.write("about to make the fig and run py.plot...\n")
logfile.flush()

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.plot(fig, filename='Oktoberfest_stream',auto_open=False)


logfile.write("brew_monitor.py: run py.plot successfully.")
logfile.write("About to try py.Stream before we start the loop...\n")
logfile.flush()

#start of continuous streaming section
# We will provide the stream link object the same token that's 
# associated with the trace we wish to stream to
s = py.Stream(stream_id)

#================================================================= 
# begin streaming
#=================================================================   
dt = time_delay
first_pass_log = True

logfile.write("brew_monitor.py: py.Stream was successful. ")
logfile.write("About to start the streaming loop....\n")
logfile.flush()


# streaming loop
while True:
    
   #try and stream the data
   if dt >= time_delay:
       try:
           s.open()
           send_data(s,sensor)
           dt = 0
           
           if first_pass_log:
               current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
               logfile.write(current_time+ ":")
               logfile.write("Streaming initiated at")
               logfile.write(remote_url + " \n") 
               logfile.write("Uploading bm.log to dropbox as:")
               upload_filename = "bm.running." + current_time + ".txt"
               logfile.write(upload_filename)
               logfile.flush()
               if upload_log:
                   subprocess.call([dropbox_uploader, 
                                    'upload', local_logfile, upload_filename])
               first_pass_log = False
               
       except SocketError:
           logfile.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))+ ":")
           logfile.write("No connection to perform data stream. ")
           logfile.write("Attempting to reconnect to wireless...\n")
           logfile.flush()
           os.system('./wireless_connect.sh')
   
   time.sleep(time_delay)
   dt += time_delay
 








