# Autoclicker
A simple autoclicker made in python.

# Usage:
Hold down the key stored inside the CLICK_BUTTON variable (f1 by default) to activate the autoclicker at the speed stored inside the CPS variable (10 by default). To pause, or to exit the program, press the keys stored in the variables PAUSE_BUTTON (f2 by default) and EXIT_BUTTON (f3 by default) respectively.
To customize the keybinds or the CPS (clicks per second), modify the variables seen at lines 9 to 12. (Note: The button presses are checked by the keyboard module, so ensure the keys are correctly mapped if you change keybinds.)

# Notes:
 - This program uses the modules `keyboard`, `win32api`, and `win32con`, which are not part of the Python standard library. To use it, you have to install these modules yourself. You can do this using the following commands using pip:

```bash
pip install keyboard
pip install pywin32
```

 - Since the program uses pywin32 module for efficiency and speed, it's not compatible with Mac-OS and Linux based operating systems.
 - If the CPS is set to a really high value, certain websites or programs might not detect the clicks. You have to lower the value if this happens.
