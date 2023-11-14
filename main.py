from playsound import playsound
from pynput.keyboard import Listener, Key
from random import randint


def on_press(key):
    if key == Key.backspace:
        playsound("sfx/backspace.wav", False)
    elif key == Key.enter:
        playsound("sfx/toop.wav", False)
    else:
        playsound(f"sfx/click{randint(1, 3)}.wav", False)


if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        listener.join()
