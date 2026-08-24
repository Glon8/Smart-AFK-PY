from .values import op
from .helpers import switch
from .visuals import render
from .helpers import config_parse_reread, read_file, write_file, getDir


# ===================================< KILL SWITCH
def ks_switch():
    ks = op['ks']
    op['afk']['stat'] = False

    switch(ks, 'stat')

    if ks['stat']:
        config_parse_reread(read_file('config.json'))
    else:
        write_file(getDir(), 'config.json', op)

    render()
