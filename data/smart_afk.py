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
    sett = afk['.settings']
    ntr = sett['.max_interactions']

    sett['.max_interactions'] = 6 if ntr < 1 else ntr

    interactions = random.randint(1, sett['.max_interactions'])

    console.print(_SEPERATOR + f' Keys Auto AFK Sequence')
    # perform the task
    for i in range(interactions):
        rand_key = random.randint(0, len(sett['.selection_string']) - 1)

        key_press(sett['.selection_string'][rand_key],
                  int(sett['.min_delay'] + disturbance(afk)),
                  int(sett['.max_delay'] + disturbance(afk)))

        timeout(int(sett['.min_delay'] + disturbance(afk)), int(sett['.max_delay'] + disturbance(afk)))
    # reset timer if still working
    if op['ks']['stat'] and afk['stat']:
        limit_validation()

        _Time = random.randint(int(sett['.min_waiting_time'] * 60), int(sett['.max_waiting_time'] * 60))

        afk['time'] = time_to_read(_Time)

        render()

        _Timer = threading.Timer(_Time, afk_reset_timer)
        _Timer.start()


def smartAFK_prot():
    global _Timer
    global _SOFT_LOCK

    afk = op['afk']
    sett = afk['.settings']

    if not op['ks']['stat'] or not afk['stat']:
        if _Timer and _Timer.is_alive():
            _Timer.cancel()
            _SOFT_LOCK = False

        return

    global _Time

    if not _SOFT_LOCK:
        _SOFT_LOCK = True

        limit_validation()

        _Time = random.randint(int(sett['.min_waiting_time'] * 60), int(sett['.max_waiting_time'] * 60))

        afk['time'] = time_to_read(_Time)

        render()

        _Timer = threading.Timer(_Time, afk_reset_timer)
        _Timer.start()
