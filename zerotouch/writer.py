"""
Config writer with telnet connection via MOXA NPort.
MOXA NPort has to be work in TCP Server mode.
"""

import logging
import time
from rich import print, inspect
from pprint import pprint as pp
from scrapli.driver import GenericDriver
from telnetlib import Telnet

# logging setup
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger("__name__")


#
def _on_console_open(cls):
    """
    Push the console when connected:
    When telnet connection has established MOXA waiting for "Enter" click
    """
    time.sleep(1)
    cls.channel.send_input("\r")
    cls.channel.send_input("term length 0")
    time.sleep(1)


# connections params
port = 4009
connect_params = {
    "host": "10.252.135.35",
    "port": port,
    "transport": "telnet",
    "auth_bypass": True,
    "on_open": _on_console_open,
}


with GenericDriver(**connect_params) as conn:
    print(f'\nConnected to: {conn.get_prompt()}\n')
    conn.send_command("enable")
    result = conn.send_commands(["show invent", "show ip int bri"])
    print(result[0].result, "\n")
    print(result[1].result, "\n")
    run_config = conn.send_command("show run")
    print(run_config.result)
