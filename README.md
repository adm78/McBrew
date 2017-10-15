#McBrew 
A series of Python scripts for recording and remotely
monitoring fermenter temperature evolutions using an
[MCP9808 thermal sensor](https://learn.adafruit.com/adafruit-mcp9808-precision-i2c-temperature-sensor-guide/overview),
compatible with Rasperry Pi and Arduino hardware.

## Pre-requisites
In order for the monitor to work, you'll have to
1. Set up an account with plot.ly[\
plot.ly](https://plot.ly/) to download the relevant keys and access your the live stream. 
2. Install the MCP9808 Python library (see [here](https://learn.adafruit.com/mcp9808-temperature-sensor-python-library/software) for details)
3. Download and Set-up [Dropbox Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) (optional, used for writing debug statement to a remote logfile)

## Starting the monitor
The monitor can be started using 
```shell
./brew_monitor.py 
```
which will live stream data from an MCP9808 thermal sensor to your account on [plot.ly](https://plot.ly/). 



```auto_start_bm.py``` is a example script that can be edited with the
relevant file paths. Putting the full path of ```auto_start_bm.py```
at the bottom of the file ```/etc/rc.local``` will automatically
start the monitoring to run when operating system boots up.

```wireless_connect.sh``` is called when a network connection is
lost. You can edit this to file such that it tries to re-connect to
your particular network, or you can just leave it as it is and it
won't do anything.

Tested with Python 2.7.*. 
