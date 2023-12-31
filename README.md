<img src="https://img.shields.io/badge/Python-3.7-blue.svg"><img src="https://img.shields.io/badge/Python-3.8-blue.svg"><img src="https://img.shields.io/badge/Python-3.9-blue.svg"><img src="https://img.shields.io/badge/Python-3.10-blue.svg">



## huawei_file_transfer

​		huawei_file_transfer is a module dedicated to Huawei device file transfer, which provides PUT and GET transfer methods in a friendly manner. In addition, it also supports file verification, and the file verification method is selected as "Compare file size" instead of "Compare MD5 hash values" because Huawei devices do not support directly generating MD5 hash values for files on the command line.



### Installing

```powershell
pip install huawei_file_transfer
```

## Example Usage

### Using the put of direction

```python
from huawei_file_transfer import file_transfer
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "host": "192.168.0.253",
    "username": "admin123",
    "password": "Huawei@123",
}

with ConnectHandler(**device_info) as net_conn:
    output = file_transfer(
        net_conn,
        source_file="s5735-l1-v200r022sph150.pat",
        dest_file="s5735-l1-v200r022sph150.pat",
        file_system="flash:",
        direction="put",
        verify_file=False,
        overwrite_file=True,
    )
    print(output)
```

**Results**

```dict
{'file_exists': True, 'file_transferred': True, 'file_verified': False}
```

### Using the get of direction

```python
from huawei_file_transfer import file_transfer
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "host": "192.168.0.253",
    "username": "admin123",
    "password": "CASJcatl@1024",
}

with ConnectHandler(**device_info) as net_conn:
    output = file_transfer(
        net_conn,
        source_file="s5735-l1-v200r022sph150.pat",
        dest_file="s5735-l1-v200r022sph150.pat",
        file_system="flash:",
        direction="get",
        verify_file=False,
        overwrite_file=True,
    )
    print(output)
```

**Results**

```dict
{'file_exists': True, 'file_transferred': True, 'file_verified': False}
```

### Using process_bar functions to display the progress of transferring files in real time

```python
from huawei_file_transfer import file_transfer,progress_bar
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "host": "192.168.0.253",
    "username": "admin123",
    "password": "Huawei@123",
}

with ConnectHandler(**device_info) as net_conn:
    output = file_transfer(
        net_conn,
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

**Results**

```text
Transferring file: s5735-l1-v200r022sph150.pat



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>| (100.00%)

{'file_exists': True, 'file_transferred': True, 'file_verified': False}
```

### Verify the file

```python
from huawei_file_transfer import file_transfer,progress_bar
from netmiko import ConnectHandler

device_info = {
    "device_type": "huawei",
    "host": "192.168.0.253",
    "username": "admin123",
    "password": "Huawei@123",
}

with ConnectHandler(**device_info) as net_conn:
    output = file_transfer(
        net_conn,
        source_file="s5735-l1-v200r022sph150.pat",
        dest_file="s5735-l1-v200r022sph150.pat",
        file_system="flash:",
        direction="get",
        verify_file=True,
        overwrite_file=True,
        progress=progress_bar
    )
    print(output)
```

**Results**

```text
Transferring file: s5735-l1-v200r022sph150.pat



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>| (100.00%)

{'file_exists': True, 'file_transferred': True, 'file_verified': True}
```

