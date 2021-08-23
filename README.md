# On-Box Node Configuration Script

Add the following files to your /bootflash/guest-share/

Turn on iox and guestshell first.

Create:
ROUTER1#guestshell run bash                                      
[guestshell@guestshell ~]$ vi /bootflash/guest-share/node-cfg.py

[guestshell@guestshell ~]$ vi /bootflash/guest-share/nodes.csv 

Run:
guestshell run python3 /bootflash/guest-share/node-cfg.py

![image](https://user-images.githubusercontent.com/63618040/130510690-acf8d514-c58d-4c5a-9393-70259b1d4e0f.png)
