<img src="https://img.shields.io/badge/Python-3.6-blue.svg">
<img src="https://img.shields.io/badge/Python-3.7-blue.svg">
<img src="https://img.shields.io/badge/Python-3.8-blue.svg">
<img src="https://img.shields.io/badge/Python-3.9-blue.svg">


##huawei_file_transfer
huawei_file_transfer is a Netmiko-based function that provides file transfer capabilities for Huawei devices. This function is modified for netmiko==4.2.0, so the version of netmiko needs to be >=4.0.0.At the same time, it provides hidden verification of the available size of the target space and the existence of files
This function currently does not support file verification, The parameter of verify needs to be set to False.
###Installing
```commandline
pip install huawei_file_transfer
```
##Example Usage
###Using the put of direction
```python3
from huawei_file_transfer import file_transfer
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "ip": "192.168.0.253",
    "username": "admin123",
    "password": "Huawei@123",
}


with ConnectHandler(**device_info) as connect:
    print("已经成功登陆设备" + device_info['ip'])
    output = file_transfer(
        connect,
        source_file="s5735-l1-v200r022sph150.pat",
        dest_file="s5735-l1-v200r022sph150.pat",
        file_system="flash:",
        direction="put",
        verify_file=False,
        overwrite_file=True,
    )
    print(output)
```
Results
```dict
{'file_exists': True, 'file_transferred': True, 'file_verified': False}
```
###Using the get of direction
```python3
from huawei_file_transfer import file_transfer
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "ip": "192.168.0.253",
    "username": "admin123",
    "password": "Huawei@123",
}


with ConnectHandler(**device_info) as connect:
    print("已经成功登陆设备" + device_info['ip'])
    output = file_transfer(
        connect,
        source_file="s5735-l1-v200r022sph150.pat",
        dest_file="s5735-l1-v200r022sph150.pat",
        file_system="flash:",
        direction="get",
        verify_file=False,
        overwrite_file=True,
    )
    print(output)
```
Results
```dict
{'file_exists': True, 'file_transferred': True, 'file_verified': False}
```
###Using process_bar functions to display the progress of transferring files in real time
```python3
from huawei_file_transfer import file_transfer,progress_bar
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "ip": "192.168.0.253",
    "username": "admin123",
    "password": "Huawei@123",
}


with ConnectHandler(**device_info) as connect:
    print("已经成功登陆设备" + device_info['ip'])
    output = file_transfer(
        connect,
        source_file="s5735-l1-v200r022sph150.pat",
        dest_file="s5735-l1-v200r022sph150.pat",
        file_system="flash:",
        direction="get",
        verify_file=False,
        overwrite_file=True,
        progress=progress_bar
    )
    print(output)
```
Results
```text
Transferring file: s5735-l1-v200r022sph150.pat

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>| (100.00%)
{'file_exists': True, 'file_transferred': True, 'file_verified': False}
```