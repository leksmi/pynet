from getpass import getpass
from rich import print, inspect
from ciscoconfparse import CiscoConfParse
from scrapli.driver.core import IOSXEDriver
from scrapli.exceptions import ScrapliAuthenticationFailed

DEVICES = {
    'bras_1': '10.252.128.51',
    'bras_2': '10.252.192.52'
}

connection_params = {
    'auth_username': input('\nusername: '),
    'auth_password': getpass('password: '),
    'auth_strict_key': False,
}


def get_device_config(ip_mgmt: str) -> str:
    """
    Retrieving  config from device
    :param ip_mgmt: str with ip_mgmt
    :return config: str with configuration
    """
    with IOSXEDriver(host=ip_mgmt, **connection_params) as conn:
        print(f'Connected to: {conn.get_prompt()}')
        result_obj = conn.send_command('show run')
    return result_obj.result


configs = {}

for device in DEVICES:
    try:
        config = get_device_config(DEVICES[device])
        configs[device] = config
    except ScrapliAuthenticationFailed as err:
        print(f'\nCould not connect to {device} with error: {err} !')
        continue

for dev in configs:
    print('\n' * 3, configs[dev])
