# Smart-AFK

**Smart-AFK** is a Python utility extracted from the older **CustomKeys** project. It repeatedly executes a configurable sequence of key presses from a provided string.

The utility includes a built-in timer that restarts the sequence after each cycle, allowing periodic keyboard input while the user is away from the PC.

## Features

* Repeatedly executes configurable keyboard input
* Built-in timer between input cycles
* Randomized waiting time between cycles
* Randomized number of key presses per cycle
* Randomized delay between individual key presses
* Double-safe key bindings to prevent accidental activation
* Configurable through `config.json`
* Simple console UI
* Optional emoji-based UI for consoles that support emojis
* Supports special keyboard keys
* Supports sequences of keys

## Requirements

* Python **3.12.6 or higher** when activating the program through a code editor
* `pynput`
* `rich`

Install the required packages with:

```bash
pip install pynput rich
```

## Usage

1. Download the project files.
2. Build the program with **PyInstaller**.
3. Run the program for the first time. A `config.json` file will be created.
4. Make sure the **kill switch is off**.
5. Open `config.json` and configure the settings if needed. This step can be skipped if the default settings are suitable.
6. Activate the kill switch to start Smart-AFK.

## `config.json` Guide

### `display`

Controls whether the console interface uses emojis or plain text.

### `key_[...]`

Configures the keyboard bindings used by the program.

It is recommended to use at least two keys together for important triggers to prevent accidental activation.

#### Special keys that are supported:

```text
tab, alt, alt_gr, shift, ctrl, cmd, 
space, enter, esc, caps, backspace, delete, 
insert, home, end, page_up, page_down, 
up, down, left, right, 
print_screen, scroll_lock, pause, menu, num_lock, 
f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12
```

> **Note:** You can add more special keys, in `special_keys.py` file.

### `.[min/max]_waiting_time`

Sets the minimum and maximum waiting time between input cycles.

The values are specified in **minutes**. Decimal values can be used, allowing fractions of a minute such as:

```text
0.5
0.1
```

The actual waiting time is randomized between the configured minimum and maximum values.

### `.max_interactions`

Sets the maximum number of keys Smart-AFK may press during a cycle.

The actual number of key presses is randomized and will always be at least **one**.

### `.selection_string`

Defines all keys that Smart-AFK is allowed to press, separated by `,`.

> **Note:** NO SPACE NEEDED IN BETWEEN

For example:

```json
"selection_string": "w,a,s,d"
```

To add chaining, you should use `+`.

For example:

```json
"selection_string": "shift+w,a,s,d"
```

> **Note:** In the example, the first key is a sequence of, `Shit` and `w`, which result in `W`.

### `.[min/max]_delay`

Sets the minimum and maximum delay between individual key presses.

The values are specified in **milliseconds**.

For example:

```text
min_delay = 100
max_delay = 500
```

The delay is randomized between the configured limits.

> **Warning:** Setting the delay too low may result in input being detected as unnatural by some applications or anti-cheat systems.

### `time`

Displays the current waiting time until the next input cycle while Smart-AFK is active.

### `.max_disturbance`

Sets the maximum limit of disturbance between individual key presses.

The values are specified in **milliseconds**.

## Project Status

**Finished**
