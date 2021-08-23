# On-Box Node Configuration Script

The following script will allow you to import pre-defined device variables and then generate the configurations for them on-box.  It then commits the configuration to running and startup configurations.

First turn on iox and guestshell first for your specific platform.

Add the following files from the repository to your devices:  /bootflash/guest-share/

ROUTER1# guestshell run bash                                      
[guestshell@guestshell ~]$ vi /bootflash/guest-share/node-cfg.py

[guestshell@guestshell ~]$ vi /bootflash/guest-share/nodes.csv 

Run:

ROUTER1# guestshell run python3 /bootflash/guest-share/node-cfg.py

![image](https://user-images.githubusercontent.com/63618040/130510690-acf8d514-c58d-4c5a-9393-70259b1d4e0f.png)
