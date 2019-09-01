
from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter your SSH username')
password = getpass()

with open ('command_file') as cmd_file:
    command_to_send = cmd_file.read().splitlines()

with open('devices') as dev_file:
    devices_ip = dev_file.read().splitlines()
try:
    for each_ip in devices_ip:
        print('Connecting to '+each_ip)
        ios_device = {
            'device_type': 'cisco_ios',
            'host': each_ip,
            'username': username,
            'password': password
        }

        net_connect = ConnectHandler(**ios_device)
        output = net_connect.send_config_set(command_to_send)
        print(output)

except ValueError:
    print('Name of the device_type is incorrect\n')
    print('kindly check\n\n\n\n')
except KeyboardInterrupt:
    print('Interuption of keyboard from the user')
except:
    print('Something else happened\n')