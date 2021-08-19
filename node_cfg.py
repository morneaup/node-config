import csv

# Define Node Source File
source_file = 'nodes.csv'

# Read Node source file into variables
with open(source_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    nodes = []
    loopback0s = []
    tunnel0s = []
    for row in reader:
        node = row['Node']
        loopback = row['Loopback0']
        tunnel0 = row['Tunnel0']
        nodes.append(node)
        loopback0s.append(loopback)
        tunnel0s.append(tunnel0)

print('Node Generation Script')
print('-' * 55)

# Validate Node number
while True:
    try:
        node_value = input('Please enter a Node ID# (1-122): ')
        if 0 >= int(node_value) < 122:
            raise ValueError
        node_idx = int(node_value) - 1
        break
    except ValueError:

        print('Warning: Not valid node number! ')

# Write Node Configuration
dst_file = ('node' + node_value + '.cfg')
with open(dst_file, 'a') as f:
 f.write(f'hostname NODE{nodes[node_idx]}\n')
 f.write('interface loopback 0\n')
 f.write(f' ip address {loopback0s[node_idx]} 255.255.255.255\n')
 f.write('interface tunnel 0\n')
 f.write(f' ip address {tunnel0s[node_idx]} 255.255.255.252\n')

# Print Instructions
print('')
print('Node configuration generated!')
print("Run the following commands to commit changes: ")
print('-' * 55)
print(' copy bootflash:/guest-share/' + dst_file + ' running-config')
print(' copy run start') 
