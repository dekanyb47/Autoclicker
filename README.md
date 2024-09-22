# Autoclicker
A simple autoclicker made in python. For added speed and efficency, the program uses the `threading` and `keyboard` modules when checking for key presses, which is done in a different thread, and the `win32api` and `win32con` modules when performing clicks.

# Usage:
Hold down the key stored inside the CLICK_BUTTON variable (f1 by default) to activate the autoclicker at the speed stored inside the CPS variable (10 by default). To pause, or to exit the program, press the keys stored in the variables PAUSE_BUTTON (f2 by default) and EXIT_BUTTON (f3 by default) respectively.
To customize the keybinds or the CPS (clicks per second), modify the variables seen at lines 9 to 12. (Note: The button presses are checked by the keyboard module, so ensure the keys are correctly mapped if you modify keybinds.)

# Notes:
 - The modules `keyboard`, `win32api`, and `win32con` are not part of the Python standard library. To use it, you have to install these modules yourself. Using pip, you can do this by running the following commands in cmd:

```bash
pip install keyboard
```

```bash
pip install pywin32
```

 - Since the program uses pywin32, it's not compatible with Mac-OS and Linux based operating systems.
 - If the CPS is set to a really high value, certain websites or programs might not detect the clicks. You have to lower the value if this happens.
 - Due to timing limitations, the higher you set the CPS, the more the realistic speed is going to differ. However, this only gets noticeable at extremely high CPS values:
     | Expected CPS | Realistic CPS |
     | ------------ | ------------- |
     | 10           | 10            |
     | 50           | 47            |
     | 250          | 175           |
     | 500          | 261           |
