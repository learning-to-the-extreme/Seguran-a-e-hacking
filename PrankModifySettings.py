import pyautogui

# Invert the mouse movement (comment out to disable)
pyautogui.FAILSAFE = False
pyautogui.mouseDown = pyautogui.mouseUp
pyautogui.mouseUp = pyautogui.mouseDown

# Swap the 'a' and 'b' keys (comment out to disable)
def swap_a_b(event):
    if event.Ascii == ord('a'):
        event.Ascii = ord('b')
    elif event.Ascii == ord('b'):
        event.Ascii = ord('a')
    return True

# Hook the key press event
hm = pyHook.HookManager()
hm.KeyDown = swap_a_b
hm.HookKeyboard()

# Run the script
pythoncom.PumpMessages()
