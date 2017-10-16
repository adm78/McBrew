<a><img src="https://user-images.githubusercontent.com/17439476/31613823-3638b88e-b27c-11e7-9b7d-7b078defd17c.png"
 alt="McBrew Logo" title="McBrew" align="left" /></a>
# McBrew 

A series of Python scripts for recording and remotely
monitoring temperatures (from your browser) using an
[MCP9808 thermal sensor](https://learn.adafruit.com/adafruit-mcp9808-precision-i2c-temperature-sensor-guide/overview),
compatible with Rasperry Pi and Arduino hardware.
![image not found](https://user-images.githubusercontent.com/17439476/31589225-170a64f2-b1f6-11e7-8831-f844d6857640.jpg)

## Pre-requisites
In order for the monitor to work, you'll have to
1. Set up an account with plot.ly[\
plot.ly](https://plot.ly/) to download the relevant keys and access your the live stream. 
2. Install the MCP9808 Python library (see [here](https://learn.adafruit.com/mcp9808-temperature-sensor-python-library/software) for details)
3. Download and set-up [Dropbox Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) (optional, used for writing debug statement to a remote logfile)
4. Edit the relevant user defined paths at the top of ```brew_monitor.py```

## Starting the monitor
The monitor can be started using 
```shell
./brew_monitor.py 
```
which will live stream data from an MCP9808 thermal sensor to your account on [plot.ly](https://plot.ly/). 


## Additional stuff
```auto_start_bm.py``` is an example script to auto start the monitor when you machine is switched on. To use it, you'll need edit the relevant paths to point to the McBrew directory. Putting the full path of ```auto_start_bm.py```
at the bottom of the file ```/etc/rc.local``` will automatically
start the monitoring to your machine is booted.

```wireless_connect.sh``` is called when the network connection is
lost. You can edit this file such that it tries to re-connect to
your network of choice, or you can just leave it as it is and it
won't do anything!

Tested with Python 2.7.*. 
