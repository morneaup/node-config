import csv
import os
#import cli

# Define Node Source File
source_file = 'nodes.csv'
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

# Read Node source file into variables
with open(source_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    nodes = []
    loopback0s = []
    loopback1s = []
    loopback2s = []
    tunnel0s = []
    for row in reader:
        node = row['Node']
        loopback0= row['Loopback0']
        loopback1 = row['Loopback1']
        loopback2 = row['Loopback2']
        tunnel0 = row['Tunnel0']
        nodes.append(node)
        loopback0s.append(loopback0)
        loopback1s.append(loopback1)
        loopback2s.append(loopback2)
        tunnel0s.append(tunnel0)
        indexCount = indexCount + 1 

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

# Tests for file exisitance
def removeFile(dst_file): 
    if os.path.exists(dst_file):
        os.remove(dst_file)
    else:
        pass

# Write New Node Configuration
dst_file = ('node' + node_value + '.cfg')
removeFile(dst_file)

# Create node configuration file
with open(dst_file, 'a') as f:
 f.write(f'hostname NODE{nodes[node_idx]}\n')
 f.write('interface loopback 0\n')
 f.write(f' ip address {loopback0s[node_idx]} 255.255.255.255\n')
 f.write('interface loopback 1\n')
 f.write(f' ip address {loopback1s[node_idx]} 255.255.255.255\n')
 f.write('interface loopback 2\n')
 f.write(f' ip address {loopback2s[node_idx]} 255.255.255.255\n')
 f.write('interface tunnel 0\n')
 f.write(f' ip address {tunnel0s[node_idx]} 255.255.255.252\n')
 f.close

# Print destination file name
print(f'Configuration generated: {dst_file}')

responseQ = yes_or_no()
if responseQ == True:
    #cli.execute(f'copy {dst_file} running-config')
    #cli.execute('copy running-config startup-config')
    print('-' * 55)
    print("The configurations have been commited to running-config and startup-config!")
else: 
    # Print Instructions
    print('')
    print("You will need to run the following commands to commit changes: ")
    print('-' * 55)
    print(' copy bootflash:/guest-share/' + dst_file + ' running-config')
    print(' copy running-config startup-config') 

exit()
