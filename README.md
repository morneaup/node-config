# Cisco On-Box Device Configuration Python Script

The following script will allow to generate a on-box device configuration based on a list of pre-defined device properites (loopback, tunnel, etc) from a imported nodes.csv file.  The user runs the script and selects the particular "Node" # they want to deployed.   The predefined settings are creating in a node#cfg file.  The user then has the option to commint the configuration to the running and startup configurations.

First turn on iox and guestshell for your specific platform.

![image](https://user-images.githubusercontent.com/63618040/130515090-2b8c7322-b619-4134-b014-88833d681d3a.png)

Add the following files from the repository to your devices:  /bootflash/guest-share/

ROUTER1# guestshell run bash                                      
[guestshell@guestshell ~]$ vi /bootflash/guest-share/node-cfg.py

[guestshell@guestshell ~]$ vi /bootflash/guest-share/nodes.csv 

Run:

ROUTER1# guestshell run python3 /bootflash/guest-share/node-cfg.py

![image](https://user-images.githubusercontent.com/63618040/130510690-acf8d514-c58d-4c5a-9393-70259b1d4e0f.png)
