import copy
import os
import sys
import json
import time
import random

from pathlib import Path
from pynput.keyboard import Controller as K

from .values import op

k = K()


# ===================================< SWITCH
# dic - dictionary to use
# key - from the dictionary to flip
def switch(dic, key):
    dic[key] = 1 - dic[key]


# ===================================< KEY PRESS
# key - to press
# delay - between press and release
def key_press(key, min_delay, max_delay):
    if not isinstance(min_delay, int) or not isinstance(max_delay, int):
        return

    if min_delay > max_delay:
        min_delay, max_t = max_delay, min_delay

    k.press(key)

    timeout(min_delay, max_delay)

    k.release(key)


# ===================================< FILES COUNT
def files_count(file_path):
    return sum(len(files) for _, _, files in os.walk(file_path))


# ===================================< GET DIRECTORY
def getDir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))

    return str(Path(__file__).resolve().parent.parent)


# ===================================< WRITE FILE
def write_file(file_path, file_name, data):
    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return None

    with open(f'{file_path}/{file_name}', 'w') as file:
        json.dump(data, file, indent=4)


# ===================================< READ FILE
# file_path - to read from
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


# ===================================< CONFIG PARSER
# string - to pars in to config
def config_parse(string):
    if string == '' or string is None:
        write_file(getDir(), 'config.json', op)
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    for name, value in config_pack.items():
        for key, val in value.items():
            if key != 'name' and name != 'ks':
                op[name][key] = val


# ===================================< CONFIG PARSER ON REREAD
# string - to pars in to config
def config_parse_reread(string):
    if string == '' or string is None:
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    valid_keys = ['display', '.positive_emoji', '.negative_emoji', 'key_trigger',
                  '.min_waiting_time', '.max_waiting_time', '.max_interactions', '.selection_string',
                  '.min_delay', '.max_delay', '.max_disturbance', 'time']

    for name, value in config_pack.items():
        for key, val in value.items():
            if key in valid_keys and op[name][key] != val and name != 'ks':
                print(f'[{name}:{key}] {val}')
                op[name][key] = val


# ===================================< UNICODE CONVERT

def unicode_convert(unicode):
    return chr(int(unicode[2:], 16))


# ===================================< TIME TO READ (afk)
def time_to_read(seconds):
    if not isinstance(seconds, int) and seconds < 0:
        return

    return f'{int(seconds / 60):02d}:{int(seconds % 60):02d}'


# ===================================< LIMIT VALIDATION (afk)
def limit_validation():
    afk = op['afk']

    min_w = afk['.min_waiting_time']
    max_w = afk['.max_waiting_time']

    if min_w < 0:
        afk['.min_waiting_time'] = 2
        min_w = afk['.min_waiting_time']

    if max_w < 0:
        afk['.max_waiting_time'] = 3.5
        max_w = afk['.max_waiting_time']

    if min_w > max_w:
        min_w, max_w = max_w, min_w

        afk['.min_waiting_time'] = min_w
        afk['.max_waiting_time'] = max_w


# ===================================< TIMEOUT (afk)
def timeout(min_t, max_t):
    if not isinstance(min_t, int) or not isinstance(max_t, int):
        return

    if min_t > max_t:
        min_t, max_t = max_t, min_t

    timeout = random.randint(min_t, max_t) / 1000
    time.sleep(timeout)


# ===================================< DISTURBANCE (afk)
def disturbance():
    afk = op['afk']

    if not afk['.max_disturbance'] or not isinstance(afk['.max_disturbance'], int):
        op['afk']['.max_disturbance'] = 100

    return random.randint(0, op['afk']['.max_disturbance'])
