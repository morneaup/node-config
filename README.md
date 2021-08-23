# On-Box Node Configuration Script

Add the following files to your /bootflash/guest-share/

Create:
ROUTER1#guestshell run bash                                      
[guestshell@guestshell ~]$ vi /bootflash/guest-share/node-cfg.py 
[guestshell@guestshell ~]$ vi /bootflash/guest-share/nodes.csv 

Run:
guestshell run python3 /bootflash/guest-share/node-cfg.py
