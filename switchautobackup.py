from netmiko import ConnectHandler
import time

#EX: tftpip = 'X.X.X.X'
tftpip = 'TFTP IP ADDRESS'

#********** Fortigate ***********

ip = 'X.X.X.X'
settings = {'ip': ip,
            'device_type': 'fortinet',
            'username': 'USERNAME',
            'password': 'PASSWORD'}

net_connect = ConnectHandler(**settings)
print("Connecting to " + ip + " ******************")
output = net_connect.send_command_timing('execute backup config tftp ' + ip + '.cfg ' + tftpip)
print(ip + " Backup Complete. ")
net_connect.disconnect()
time.sleep(2)

#********** ARUBA ***********

ip = 'X.X.X.X'
settings = {'ip': ip,
#            'device_type': 'hp_comware',
            'device_type': 'hp_procurve',
            'username': 'USERNAME',
            'password': 'PASSWORD'}

net_connect = ConnectHandler(**settings)
print("Connecting to " + ip + " ******************")
output = net_connect.send_command_timing('backup startup-configuration to ' + tftpip + ' ' + ip + '.cfg')
print(ip + " Backup Complete. ")
net_connect.disconnect()
time.sleep(2)

#********** HP 1950 ***********

ip = 'X.X.X.X'
settings = {'ip': ip,
            'device_type': 'hp_procurve',
            'username': 'USERNAME',
            'password': 'PASSWORD'}

net_connect = ConnectHandler(**settings)
print("Connecting to " + ip + " ******************")
output = net_connect.send_command_timing('xtd-cli-mode')
output = net_connect.send_command_timing('y')
output = net_connect.send_command_timing('foes-bent-pile-atom-ship')
output = net_connect.send_command_timing('backup startup-configuration to ' + tftpip + ' ' + ip + '.cfg')
print(ip + " Backup Complete. ")
net_connect.disconnect()
time.sleep(2)

#********** HP 1920 ***********

ip = 'X.X.X.X'
settings = {'ip': ip,
            'device_type': 'hp_procurve',
            'username': 'USERNAME',
            'password': 'PASSWORD'}

net_connect = ConnectHandler(**settings)
print("Connecting to " + ip + " ******************")
output = net_connect.send_command_timing('enable')
output = net_connect.send_command_timing('copy nvram:startup-config tftp://' + tftpip + '/' + ip + '.cfg')
output = net_connect.send_command_timing('y')
print(ip + " Backup Complete. ")
net_connect.disconnect()
time.sleep(2)

#********** HP 1910 ***********

ip = 'X.X.X.X'
settings = {'ip': ip,
            'device_type': 'hp_procurve',
            'username': 'USERNAME',
            'password': 'PASSWORD'}

net_connect = ConnectHandler(**settings)
print("Connecting to " + ip + " ******************")
output = net_connect.send_command_timing('_cmdline-mode on')
output = net_connect.send_command_timing('y')
output = net_connect.send_command_timing('512900')
output = net_connect.send_command("tftp " + tftpip + " put startup.cfg " + ip + ".cfg")
print(ip + " Backup Complete. ")
net_connect.disconnect()
time.sleep(2)

#********** Cisco ***********

ip = 'X.X.X.X'
settings = {'ip': ip,
            'device_type': 'cisco_ios',
            'username': 'USERNAME',
            'password': 'PASSWORD'}

net_connect = ConnectHandler(**settings)
print("Connecting to " + ip + " ******************")
output = net_connect.send_command_timing("copy startup-config tftp://" + tftpip + "/" + ip + ".cfg")
print(ip + " Backup Complete. ")
net_connect.disconnect()
time.sleep(2)

