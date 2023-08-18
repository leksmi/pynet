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
    Логин на устройство, чтение конфигурации,
    запись конфигурации в текущий каталог.
    (класс CiscoConfParse считывает конфиг именно из файла на диске!)
    :param ip_mgmt: str with ip_mgmt
    :return config: str with configuration
    """
    with IOSXEDriver(host=ip_mgmt, **connection_params) as conn:
        print(f'Connected to: {conn.get_prompt()}')
        result_obj = conn.send_command('show run')
    return result_obj.result


def config_generator(parser_obj: CiscoConfParse.find_objects) -> list:
    """
    It get object from CiscoConfParse parser,
    then generates commands list
    :param parser_obj: CiscoConfParse.find_objects element
    :return:
    """
    commands_block = [parser_obj.parent.text]
    for child in parser_obj.children:
        commands_block.append(child.text)
    return commands_block


for device in DEVICES:
    try:
        config = get_device_config(DEVICES[device])
        configs[device] = config
    except ScrapliAuthenticationFailed as err:
        print(f'\nCould not connect to {device} with error: {err} !')
        continue
