import pyautogui
import os
from settings import delay
from settings import resume_key
from settings import pause_key
from settings import exit_key
from pynput.keyboard import *

os.system('title kryyaa`s clicker')


pause = True
running = True

os.system('cls')

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker By kryyaa#2740 (discord) / @kryyaasoft (telegram)\n")
    print("// - Settings: ")
    print(f"\t delay = {delay}\n")
    print("// - Controls:")
    print(f"\t {resume_key} = Resume")
    print(f"\t {pause_key} = Pause")
    print(f"\t {exit_key} = Exit")
    print("-----------------------------------------------------")
    print(f'Press {resume_key} to start ...\n')

def display_controlsRU():
    print("// Авто Кликер от kryyaa#2740 (дискорд) / @kryyaasoft (телеграм)\n")
    print("// - Настройки: ")
    print(f"\t время между кликами (милисекунды) = {delay}\n")
    print("// - Управление:")
    print(f"\t {resume_key} = Старт")
    print(f"\t {pause_key} = Пауза")
    print(f"\t {exit_key} = Выход")
    print("-----------------------------------------------------")
    print(f'Нажмите {resume_key} чтобы начать...\n')


def main():

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()

    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()

if __name__ == "__main__":
    main()