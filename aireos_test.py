from collections import namedtuple
from pprint import pprint as pp
from getpass import getuser
from getpass import getpass
from rich import print, inspect
from scrapli import Scrapli
from scrapli_community.cisco import aireos


dev_template = {
    "platform": "cisco_aireos",
    "auth_username": getuser(),
    "auth_password": getpass(),
    "auth_strict_key": False,
    "ssh_config_file": True,
}


with Scrapli(host="10.228.48.5", **dev_template) as conn:
    print(f'Connected to {conn.get_prompt().rstrip(">#")}')
    conn.send_command("config paging disable")
    ap_list = conn.send_command("show ap summ").result.splitlines()
    result = {}
    for line in ap_list:
        if "WAP" in line:
            line_list = line.split()
            result[line_list[0]] = line_list[-6]
    result = dict(sorted(result.items()))
    print(result)
