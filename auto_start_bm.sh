./wireless_connect.sh > /home/pi/bm.log
# python /home/pi/brewing/mcbrew/brew_monitor.py &> | ts '[%Y-%m-%d %h:%M:%S]' >> /home/pi/bm.log
# python /home/pi/helloworld.py >> /home/pi/bm.log 2>&1
# python /home/pi/brewing/mcbrew/brew_monitor.py >> /home/pi/bm.log 2>&1
python /home/pi/brewing/mcbrew/brew_monitor.py 2> /home/pi/bm.log
BACKUP_FILE="/home/pi/bm.crash.log.$(date +%F_%R).txt"
cp /home/pi/bm.log $BACKUP_FILE
/home/pi/software/dropbox_uploader/dropbox_uploader.sh upload $BACKUP_FILE $BACKUP_FILE