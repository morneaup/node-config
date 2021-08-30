# Cisco On-Box Device Configuration Python Script

The following script will allow you to generate a on-box device configuration based on a list of pre-defined device properites (loopback, tunnel, etc) from a imported nodes.csv file.  The user runs the script and selects the particular "Node" # they want to deployed.   The predefined settings are creating in a node configuration file.  The user then has the option to commint the configuration to the running and startup configurations.

Example Node Table:
![image](https://user-images.githubusercontent.com/63618040/130519098-9e177e8f-50ca-4d44-b041-55cd7b304e1e.png)

First turn on iox and guestshell for your specific platform.

Example IOX/Guestshell Configuration:
![image](https://user-images.githubusercontent.com/63618040/131387300-cad98980-3be1-43aa-bf5b-f5e01e8a2785.png)

Add the following files from the repository to your devices:  /bootflash/guest-share/

ROUTER1# guestshell run bash                                      
[guestshell@guestshell ~]$ vi /bootflash/guest-share/node-cfg.py

[guestshell@guestshell ~]$ vi /bootflash/guest-share/nodes.csv 

Run:

ROUTER1# guestshell run python3 /bootflash/guest-share/node-cfg.py

![image](https://user-images.githubusercontent.com/63618040/130510690-acf8d514-c58d-4c5a-9393-70259b1d4e0f.png)
