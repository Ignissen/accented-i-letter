from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys
import time
import daemon


with daemon.DaemonContext():
    prev_time_i = 0
    prev_time_I = 0
    kbd = Controller()

    def on_press(key):
        global prev_time_i, prev_time_I
        try:
            if key.char == 'i':
                if time.perf_counter() - prev_time_i < 0.2:
                    kbd.press(Key.backspace)
                    kbd.release(Key.backspace)
                    kbd.press(Key.backspace)
                    kbd.release(Key.backspace)
                    kbd.type('í')
                else:
                    prev_time_i = time.perf_counter()
            elif key.char == 'I':
                if time.perf_counter() - prev_time_I < 0.2:
                    kbd.press(Key.backspace)
                    kbd.release(Key.backspace)
                    kbd.press(Key.backspace)
                    kbd.release(Key.backspace)
                    kbd.type('Í')
                else:
                    prev_time_I = time.perf_counter()
        except AttributeError:
            pass
        

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:
        time.sleep(0.01)
    #listener.stop()