Duck Hunter 
==========

Converts a USB Rubber ducky script into a Kali Nethunter friendly format for the HID attack

Original code and concept by @binkybear

Quack

### Running Duck Hunter

From a command line, type:

```
duckhunter.py -l {us} input.txt output.sh```


Supports multiple languages: us, fr, de, es, sv, it, uk, ru, dk, no, pt, be

Output file can be run as a regular shell file on Nethunter devices.

### Keyboard Commands
Here is a list of commands that will work with your Duck Hunter input file for conversion:

```
DELAY 1000```

In miliseconds, 1000 is equal to 1 second

```
COMMAND SPACE```

Apple command key with space will load spotlight

```
GUI r```

Windows + R key to bring up run

```
WIN8CMD```

Load an elevated command line in Windows 8

```
WIN7CMD```

Load an elevated command line in Windows 7

```
WINCMD```

Load a Windows command line

```
STRING echo "I love ducky"```

We pass text we want to type with the STRING command. STRING will by default press enter at the end of line.

```
TEXT echo "I love ducky"```

TEXT is similar to STRING command but instead of pressing ENTER after text is typed, we leave text where it is.  This is useful if you want to type something then combine text with other shortcuts (e.x. TEXT cmd; CONTROL SHIFT ENTER)

Other useful commands:
```
ALT
CONTROL
CTRL
DELETE
DEL
SHIFT
MENU
APP
ESCAPE
ESC
END
SPACE
TAB
PRINTSCREEN
ENTER
UP
DOWN
LEFT
RIGHT
F1-F10
CAPSLOCK
```
Keys can also be combined into: 
```
CTRL ALT DEL```

### Mouse Commands

```
MOUSE LEFTCLICK
MOUSE RIGHTCLICK```

Left click and right click.

```
MOUSE 100 0``` 

Will move 100 pixels to right.

```
MOUSE 0 -50``` 

Will move 50 pixels up.
