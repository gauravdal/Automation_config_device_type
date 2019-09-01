from netmiko import ConnectHandler

ios_login_credentials = {
    'device_type': 'cisco_ios', #mandatory to provide device_type, ip, username, password
    'ip': '192.168.10.20',
    'username': 'gaurav',
    'password': 'VIRL'
}

net_connect = ConnectHandler(**ios_login_credentials)
output = net_connect.send_command('show ip int brief')
print(output)