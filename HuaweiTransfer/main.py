from huawei_file_transfer import file_transfer,progress_bar
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
        progress=progress_bar
    )
    print(output)