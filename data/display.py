from .values import op
from .visuals import render


# ===================================< DISPLAY SWITCH
def display_switch():
    if not op['ks']['stat']:
        return

    general = op['gnr']

    general['display'] = 'emoji' if general['display'] == 'plain' else 'plain'

    render()