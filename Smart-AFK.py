from data.helpers import config_parse, read_file
from data.values import op
from data.visuals import render
from data.killswitch import ks_switch
from data.display import display_switch
from data.smart_afk import smartAFK_switch, smartAFK_prot

from pynput.keyboard import Controller as K, Listener as kL, HotKey

k = K()


# ===================================< CONTROL PANNEL
def control_panel():
    while True:
        if op['ks']['stat']:
            smartAFK_prot()


# ===================================< MAIN
def main():
    config_parse(read_file('config.json'))

    # \/===================================< HOTKEYS SETTINGS
    hotkeys = [
        HotKey(HotKey.parse(op['gnr']['key_display_change']), display_switch),
        HotKey(HotKey.parse(op['ks']['key_trigger']), ks_switch),
        HotKey(HotKey.parse(op['afk']['key_trigger']), smartAFK_switch),
    ]

    def on_press(key):
        for thing in hotkeys:
            thing.press(key)

    def on_release(key):
        for thing in hotkeys:
            thing.release(key)

    # /\===================================< HOTKEYS SETTINGS

    render()

    with kL(on_press=on_press, on_release=on_release):
        control_panel()


# ===================================< MAIN START
if __name__ == '__main__':
    main()
