
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

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
        try:
            net_connect = ConnectHandler(**ios_device)
        except (AuthenticationException):
            print('Authentication failure to ip address: '+each_ip)
            continue
        except (NetMikoTimeoutException):
            print('Timeout to device: '+each_ip)
            continue
        except (EOFError):
            print('End of file while attempting the device: '+each_ip)
            continue
        except (SSHException):
            print('Error while making SSH connection to device: '+each_ip)
            continue
        except Exception as error:
            print('Some other error: '+error)
            continue

        output = net_connect.send_config_set(command_to_send)
        print(output)

except ValueError:
    print('Name of the device_type is incorrect\n')
    print('kindly check\n\n\n\n')
except KeyboardInterrupt:
    print('Interuption of keyboard from the user')
except Exception as error:
    print('Something else happened\n'+ error)