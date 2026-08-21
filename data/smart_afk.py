import random
import threading

from rich.console import Console

from .values import op, _SEPERATOR
from .helpers import switch, key_press, time_to_read, limit_validation, timeout, disturbance
from .visuals import render

console = Console()

_Time = 0
_Timer = None
_SOFT_LOCK = False


# ===================================< SMART AFK
def smartAFK_switch():
    if not op['ks']['stat']:
        return

    switch(op['afk'], 'stat')

    if not op['afk']['stat']:
        render()


def afk_reset_timer():
    global _Time
    global _Timer

    afk = op['afk']
    ntr = afk['.max_interactions']

    afk['.max_interactions'] = 6 if ntr < 1 else ntr

    interactions = random.randint(1, op['afk']['.max_interactions'])

    console.print(_SEPERATOR + f' Keys Auto AFK Sequence')
    # perform the task
    for i in range(interactions):
        rand_key = random.randint(0, len(op['afk']['.selection_string']) - 1)

        key_press(afk['.selection_string'][rand_key],
                  int(op['afk']['.min_delay'] + disturbance()),
                  int(op['afk']['.max_delay'] + disturbance()))

        timeout(int(op['afk']['.min_delay'] + disturbance()), int(op['afk']['.max_delay'] + disturbance()))
    # reset timer if still working
    if op['ks']['stat'] and afk['stat']:
        limit_validation()

        _Time = random.randint(int(op['afk']['.min_waiting_time'] * 60), int(op['afk']['.max_waiting_time'] * 60))

        afk['time'] = time_to_read(_Time)

        render()

        _Timer = threading.Timer(_Time, afk_reset_timer)
        _Timer.start()


def smartAFK_prot():
    global _Timer
    global _SOFT_LOCK

    afk = op['afk']

    if not op['ks']['stat'] or not afk['stat']:
        if _Timer and _Timer.is_alive():
            _Timer.cancel()
            _SOFT_LOCK = False

        return

    global _Time

    if not _SOFT_LOCK:
        _SOFT_LOCK = True

        limit_validation()

        _Time = random.randint(int(op['afk']['.min_waiting_time'] * 60), int(op['afk']['.max_waiting_time'] * 60))

        afk['time'] = time_to_read(_Time)

        render()

        _Timer = threading.Timer(_Time, afk_reset_timer)
        _Timer.start()
