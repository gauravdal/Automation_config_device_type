
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

username = input('Enter the SSH username: ')
password = getpass()

with open('devices','r') as dev_file:
    devices_ip = dev_file.read().splitlines()

with open('commands_file_switch','r') as switch_config:
    switch_cmd = switch_config.read().splitlines()

with open('commands_file_router','r') as router_config:
    router_cmd = router_config.read().splitlines()

for each_ip in devices_ip:
    print('Accessing the device: '+each_ip)

    ios_device = {
        'device_type': 'cisco_ios',
        'host': each_ip,
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print('Authentication error to device: '+each_ip)
        continue
    except (NetMikoTimeoutException):
        print('Timeout to device: '+each_ip)
        continue
    except (EOFError):
        print('End of file error to device: '+each_ip)
        continue
    except (SSHException):
        print('SSH connection error to device: '+each_ip)
        continue
    except (Exception) as error:
        print('Unknown error as: '+error)
        continue

    list_of_software = ['vios_l2-ADVENTERPRISEK9-M',
                        'VIOS-ADVENTERPRISEK9-M',
                        'C7200-SPSERVICESK9-M',
                        ]


    #checking software version
    for each_software in list_of_software:
        print('Checking for software version: '+each_software)
        software_device = net_connect.send_command('show version')
        int_version = 0 #reset value to 0
        int_version = software_device.find(each_software)
        if (int_version > 0):
            print('Device software is found: '+each_software)
            break
        else:
            print('Did not find the device software: '+each_software)

    if each_software == 'vios_l2-ADVENTERPRISEK9-M':
        output = net_connect.send_config_set(switch_cmd)
        print(output)
    elif each_software == 'VIOS-ADVENTERPRISEK9-M':
        output = net_connect.send_config_set(router_cmd)
    print(output)
