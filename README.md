# McBrew
![alt tag](https://github.com/adm78/McBrew/blob/master/UI/GUIresources/ferm_plus_therm.png)
A series of Python scripts for recording and remotely monitoring fermenter temperature evolutions. 

The most functional script for now is brew_monitor.py. This script is able to live stream data from an MCP9808 thermal sensor to plot.ly. 

brew_recorder.py is an alternative which uses the Dropbox API to stream data to a Dropbox account. The associated plotting script brew_reader.py is not yet fully functional. 

mcbrew.py is the front end GUI but, again, is not yet functional. This might be coupled with plotly at some point in the future. 

i2c_tsensor_python.py is a script that reads directly from the thermal sensor. It removes the need to install the MCP9808 python library and the temperature. This would need to packaged into a library with a public getTemperature method if you want to use it.

Works with Python 2.7.*. 
