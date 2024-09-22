# Usage: Hold down the key stored inside the CLICK_BUTTON variable (f1 by default) to activate the autoclicker at the
# speed stored inside the CPS variable (10 by default). To pause, or to exit the program, press the keys stored in
# the variables PAUSE_BUTTON (f2 by default) and EXIT_BUTTON (f3 by default) respectively.

# To customize keybinds or CPS (clicks per second), modify the variables seen below.
# (Note: The button presses are checked by the keyboard module, so ensure the keys are correctly mapped if you
# change keybinds.)

CPS = 10
CLICK_BUTTON = "f1"
PAUSE_BUTTON = "f2"
EXIT_BUTTON = "f3"


import keyboard, time, win32api, win32con, threading

def click(CPS):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5 / CPS)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def altThreadActions(pauseEvent, exitEvent, PAUSE_BUTTON, EXIT_BUTTON):
    while True:
        if keyboard.is_pressed(PAUSE_BUTTON):
            if pauseEvent.is_set():
                pauseEvent.clear()
                print("Program unpaused.")
                time.sleep(1)
            else:
                pauseEvent.set()
                print("Program paused.")
                time.sleep(1)

        if keyboard.is_pressed(EXIT_BUTTON):
            print("Exiting program...")
            exitEvent.set()
            break

        time.sleep(0.05)


def autoClicker(CPS, pauseEvent, exitEvent, CLICK_BUTTON):
    while not pauseEvent.is_set() and not exitEvent.is_set():
        while keyboard.is_pressed(CLICK_BUTTON):
            click(CPS)
            time.sleep(0.5 / CPS)
        time.sleep(0.05)


def main():
    global CPS, CLICK_BUTTON, PAUSE_BUTTON, EXIT_BUTTON

    pauseEvent = threading.Event()
    exitEvent = threading.Event()

    # Start alternative thread to check for f2 and f3 button presses.
    altThread = threading.Thread(target=altThreadActions, args=(pauseEvent, exitEvent, PAUSE_BUTTON, EXIT_BUTTON))
    altThread.start()

    print(f"Program started. Usage: Press {CLICK_BUTTON} to activate auto-clicker, {PAUSE_BUTTON} to pause or unpause, {EXIT_BUTTON} to exit the application. Current CPS: {CPS}")

    while not exitEvent.is_set():
        autoClicker(CPS, pauseEvent, exitEvent, CLICK_BUTTON)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
