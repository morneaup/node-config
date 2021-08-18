import csv
import os

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

# Validate Node number
while True:
    node_value = input('Please enter a NodeID# (1-122): ')
    try:
        node_idx = int(node_value) - 1
        break
    except ValueError:
        print('Please enter a valid number! ')

dst_file = ('node' + node_value + '.cfg')


with open(dst_file, 'a') as f:
 f.write(f'hostname NODE{nodes[node_idx]}\n')
 f.write('interface tunnel 0\n')
 f.write(f' ip address {tunnel0s[node_idx]} 255.255.255.252\n')
print('Completed!') 
