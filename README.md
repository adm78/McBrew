A series of Python scripts for recording and remotely monitoring
fermenter temperature evolutions.

The montior can be started using 
```shell
./brew_monitor.py 
```
which will live stream data from an MCP9808 thermal sensor to your account on [plot.ly](https://plot.ly/). 

You'll have to set up an account with plotly to download the relevant
keys and access your the live stream.

```auto_start_bm.py``` is a example script that can be edited with the
relevant file paths. Putting the full path of ```auto_start_bm.py```
at the bottom of the file ```/etc/rc.local``` will auto-matically
start the monitoring to run when operating system boots up.

Tested with Python 2.7.*. 
