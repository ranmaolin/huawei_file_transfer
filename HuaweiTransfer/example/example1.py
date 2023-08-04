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