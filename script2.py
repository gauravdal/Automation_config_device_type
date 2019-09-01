from netmiko import ConnectHandler

with open('command_file') as cmd_file: #opening command file and storing each line as a list
    command_to_send = cmd_file.read().splitlines()

ios_devices = {
    'device_type':'cisco_ios',
    'ip': '192.168.10.10',
    'username': 'gaurav',
    'password': 'VIRL'
}

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(command_to_send)
    print(output)