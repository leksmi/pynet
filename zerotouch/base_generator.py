"""
Base Class generator to make generic config
for different vendors
"""

cisco_generic: dict = {
    'general': [
        'service timestamps debug datetime localtime show-timezone',
        'service timestamps log datetime localtime show-timezone',
        'service password-encryption',
        'logging buffered 2048000',
    ],
    'taccacs_group': [
        'aaa group server tacacs+ GPN',
        'server name spb99-ise-psn01',
        'server name spb99-ise-psn02',
        'server name oms02-ise-psn01',
        'server name gpn-ito-nbk'
    ],
    ''
}

huawei_generic: dict = {}


class CiscoBase:
    """
    Generic Cisco IOS/IOS-XE
    """

    pass


class HuaweiBase:
    """
    Generic Huawei VRP
    """

    pass
