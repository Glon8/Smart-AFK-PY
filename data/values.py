_OPERATIONS = {
    'gnr': {
        'name': 'General',
        'note': "Display is either 'emoji' or 'plain'",
        'key_display_change': 'c+o',
        'display': 'plain',
        '.settings': {
            '.positive_emoji': "U+2705",
            '.negative_emoji': "U+274C"
        }
    },
    'ks': {
        'name': 'Kill Switch',
        'note': 'Do not abuse Kill Switch! May lower performance!',
        'key_trigger': 'c+0',
        'stat': False,
    },
    'afk': {
        'name': 'Smart AFK',
        'note': 'Remember to set Kill Switch on before use!',
        'key_trigger': 'c+2',
        'stat': False,
        'time': 0,
        '.settings': {
            '.min_waiting_time': 2,
            '.max_waiting_time': 3.5,
            '.max_interactions': 6,
            '.selection_string': 'w,a,s,d',
            '.min_delay': 178,
            '.max_delay': 300,
            '.max_disturbance': 100,
        },
    },
}

_SEPERATOR = f"===========================<"

op = _OPERATIONS
