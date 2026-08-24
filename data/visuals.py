import os
import platform

from rich.console import Console

from .values import op, _SEPERATOR
from .helpers import unicode_convert

console = Console()


# ===================================< VISUALS
def render():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    general = op['gnr']
    sett = general['.settings']

    pos = 'on' if general['display'] == 'plain' else unicode_convert(sett[".positive_emoji"])
    neg = 'off' if general['display'] == 'plain' else unicode_convert(sett[".negative_emoji"])

    for key, values in op.items():
        for att, stat in values.items():
            if not att.startswith('.'):
                if att == 'name':
                    console.print(_SEPERATOR + ' ' + str(stat))
                elif (att == 'key_trigger' or
                      att == 'note' or
                      att == 'display' or
                      att == 'key_display_change' or
                      att == 'time'):
                    console.print(f"{att} : {stat}")
                else:
                    console.print(f"{att} : {pos if stat else neg}")
