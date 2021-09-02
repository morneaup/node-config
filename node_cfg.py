# Network Node Configuration Script
# Works with Python 3.6.8
import csv
import os
import cli

# Define variables
source_file = '/bootflash/guest-share/nodes.csv'
dst_path = '/bootflash/guest-share/'
ios_path = 'bootflash:guest-share/'
indexCount = 0
node_idx = 0
node_value = 0

# Test YES/NO question
def yes_or_no():
    while "The response is invalid!":
        try:
            # Ask to commit configuration
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

# Validate nodes.csv exists
def checksource_file(source_file):
    if os.path.exists(source_file):
        pass
    else:
        print('Warning: Please create: ' + source_file)
        exit()

# Input and Validate Node number
def check_node_number(indexCount):
    while True:
        try:
            node_value = input(f'Please enter a Node ID# (1-{indexCount}): ')
            if 0 < int(node_value) <= (indexCount):
                node_idx = int(node_value) - 1
                return node_idx, node_value
            else:
                raise ValueError
        except ValueError:
            print('Warning: Not valid node number! ')

if __name__ == "__main__":
    # Read Node source file into variables
    checksource_file(source_file)
    try:
        with open(source_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Create variable arrays
            nodes = []
            loopback1s = []
            loopback2s = []
            loopback3s = []
            tunnel1s = []
            tunnel2s = []
            tunnel3s = []
            tunnel4s = []
            DataNetwork1s = []
            CallManager1s = []

            # Read in data into arrays
            for row in reader:
                try:
                    # Assign Row column name to Array
                    node = row['Node']
                    loopback1= row['Loopback1']
                    loopback2 = row['Loopback2']
                    loopback3 = row['Loopback3']
                    tunnel1 = row['Tunnel1']
                    tunnel2 = row['Tunnel2']
                    tunnel3 = row['Tunnel3']
                    tunnel4 = row['Tunnel4']
                    DataNetwork1 = row['DataNetwork1']
                    CallManager1 = row['CallManager1']
                except Exception:
                    print('Warning: Check input file format and header names!')
                    exit()
                # Append new row 
                nodes.append(node)
                loopback1s.append(loopback1)
                loopback2s.append(loopback2)
                loopback3s.append(loopback3)
                tunnel1s.append(tunnel1)
                tunnel2s.append(tunnel2)
                tunnel3s.append(tunnel3)
                tunnel4s.append(tunnel4)
                DataNetwork1s.append(DataNetwork1)
                CallManager1s.append(CallManager1)
                indexCount += 1
    except Exception:
        print('Warning: Check input file!')
        exit()
    finally:
        csvfile.close
            
    # Print Menu Header
    print('')
    print('Node Configuration Generation Script')
    print('-' * 55)

    # Call Input Node number
    node_idx , node_value = check_node_number(indexCount)

    # Write new variable paths based on input
    dst_cfg_file = (f'node{node_value}.cfg')
    full_path = (dst_path + dst_cfg_file)
    ios_full = (ios_path + dst_cfg_file)

    # Cleanup old and create new node cfg file
    removeFile(full_path)
    try:
        with open(full_path, 'a') as f:
            f.write(f'hostname NODE{nodes[node_idx]}\n')
            f.write('interface loopback 1\n')
            f.write(f' ip address {loopback1s[node_idx]} 255.255.255.255\n')
            f.write('interface loopback 2\n')
            f.write(f' ip address {loopback2s[node_idx]} 255.255.255.255\n')
            f.write('interface loopback 3\n')
            f.write(f' ip address {loopback3s[node_idx]} 255.255.255.255\n')
            f.write('interface tunnel 1\n')
            f.write(f' ip address {tunnel1s[node_idx]} 255.255.255.252\n')
            f.write('interface tunnel 2\n')
            f.write(f' ip address {tunnel2s[node_idx]} 255.255.255.252\n')
            f.write('interface tunnel 3\n')
            f.write(f' ip address {tunnel3s[node_idx]} 255.255.255.252\n')
            f.write('interface tunnel 4\n')
            f.write(f' ip address {tunnel4s[node_idx]} 255.255.255.252')
    except:
        print('Warning: Problem with output file!')
        exit()
    finally:
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
