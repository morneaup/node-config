import csv
import os
import cli

# Define variables
source_file = '/bootflash/guest-share/nodes.csv'
dst_path = '/bootflash/guest-share/'
ios_path = 'bootflash:guest-share/'
indexCount = 0

# Define YES/NO Module
def yes_or_no():
    while "The response is invalid!":
        try:
            question = input('Commit new configuration to running-config and startup-config? (y/n): ').lower().strip()
            if question == 'y':
                return True
            if question == 'n':
                return False
            else:
                raise ValueError
        except ValueError:
            print('Warning: Not valid response!')

# Tests for file exisitance
def removeFile(full_path): 
    if os.path.exists(full_path):
        os.remove(full_path)
    else:
        pass

# Read Node source file into variables
with open(source_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    nodes = []
    loopback1s = []
    loopback2s = []
    loopback3s = []
    tunnel0s = []
    for row in reader:
        node = row['Node']
        loopback1= row['Loopback1']
        loopback2 = row['Loopback2']
        loopback3 = row['Loopback3']
        tunnel0 = row['Tunnel0']
        nodes.append(node)
        loopback1s.append(loopback1)
        loopback2s.append(loopback2)
        loopback3s.append(loopback3)
        tunnel0s.append(tunnel0)
        indexCount = indexCount + 1 

# Print Menu Header
print('')
print('Node Generation Script')
print('-' * 55)

# Validate Node number
while True:
    try:
        node_value = input(f'Please enter a Node ID# (1-{indexCount}): ')
        if 0 < int(node_value) <= (indexCount):
            node_idx = int(node_value) - 1
            break
        else:
            raise ValueError
    except ValueError:
        print('Warning: Not valid node number! ')

# Write new variable paths based on input
dst_cfg_file = ('node' + node_value + '.cfg')
full_path = (dst_path + dst_cfg_file)
ios_full = (ios_path + dst_cfg_file)

# Cleanup old and create new node cfg file
removeFile(full_path)
with open(full_path, 'a') as f:
 f.write(f'hostname NODE{nodes[node_idx]}\n')
 f.write('interface loopback 1\n')
 f.write(f' ip address {loopback1s[node_idx]} 255.255.255.255\n')
 f.write('interface loopback 2\n')
 f.write(f' ip address {loopback2s[node_idx]} 255.255.255.255\n')
 f.write('interface loopback 3\n')
 f.write(f' ip address {loopback3s[node_idx]} 255.255.255.255\n')
 f.write('interface tunnel 0\n')
 f.write(f' ip address {tunnel0s[node_idx]} 255.255.255.252')
 f.close

# Print destination cfg file name for user
print('')
print(f'Configuration generated: {dst_cfg_file}')
print('')

# Do you want to commit configuration?
responseQ = yes_or_no()
if responseQ == True:
    cli.executep(f'copy {ios_full} running-config')
    cli.executep('copy running-config startup-config')
    print('-' * 55)
    print("The configurations have been commited to running-config and startup-config!")
else: 
    # Print Instructions
    print('')
    print("You will need to run the following commands to commit changes: ")
    print('-' * 55)
    print(f' copy {ios_full} running-config')
    print(' copy running-config startup-config')
    
print('')
print("Script is complete!")
exit()
