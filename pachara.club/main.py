import os
import time
import keyboard
import pyautogui
from termcolor import colored
from colorant import Colorant

#Settings
TOGGLE_KEY = 'F1'  # Toggle on/off 
XFOV = 70  # X-Axis FOV
YFOV = 70  # Y-Axis FOV
INGAME_SENSITIVITY = 0.503 # Replace this with the your in-game sensitivity value
FLICKSPEED = 1.07437623 * (INGAME_SENSITIVITY ** -0.9936827126)  # Calculate flick speed
MOVESPEED = 1 / (5 * INGAME_SENSITIVITY) # Calculate move speed

monitor = pyautogui.size()
CENTER_X, CENTER_Y = monitor.width // 2, monitor.height // 2

def main():
    os.system('title Autistic Nigga 69420')
    colorant = Colorant(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, MOVESPEED)
    print(colored(''' ██▓███   ▄▄▄       ▄████▄   ██░ ██  ▄▄▄       ██▀███   ▄▄▄            ▄████▄   ██▓     █    ██  ▄▄▄▄   
▓██░  ██▒▒████▄    ▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒████▄         ▒██▀ ▀█  ▓██▒     ██  ▓██▒▓█████▄ 
▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄       ▒▓█    ▄ ▒██░    ▓██  ▒██░▒██▒ ▄██
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██      ▒▓▓▄ ▄██▒▒██░    ▓▓█  ░██░▒██░█▀  
▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒ ██▓ ▒ ▓███▀ ░░██████▒▒▒█████▓ ░▓█  ▀█▓
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▓▒ ░ ░▒ ▒  ░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░▒▓███▀▒
░▒ ░       ▒   ▒▒ ░  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░▒    ░  ▒   ░ ░ ▒  ░░░▒░ ░ ░ ▒░▒   ░ 
░░         ░   ▒   ░         ░  ░░ ░  ░   ▒     ░░   ░   ░   ▒    ░   ░          ░ ░    ░░░ ░ ░  ░    ░ 
               ░  ░░ ░       ░  ░  ░      ░  ░   ░           ░  ░  ░  ░ ░          ░  ░   ░      ░      
                   ░                                               ░  ░                               ░     
                                              BETA TEST''', 'magenta'))
    print()
    print(colored('[Info]', 'green'), colored('Set enemies to', 'white'), colored('Purple', 'magenta'))
    print(colored('[Info]', 'green'), colored(f'Press {colored(TOGGLE_KEY, "magenta")} toggle ON/OFF ', 'white'))
    print(colored('[Info]', 'green'), colored(f'Press', 'white'), colored('F2', 'magenta'), colored('toggle ON/OFF Window Detection', 'white'))
    print(colored('[Info]', 'green'), colored('lAlt', 'magenta'), colored('= Aimbot', 'white'))
    print(colored('[Info]', 'green'), colored('X2MB', 'magenta'), colored('= Triggerbot', 'white'))
    print(colored('[Info]', 'green'), colored('X1MB', 'magenta'), colored('= Silentaim', 'white'))
    print(colored('[Info]', 'green'), colored('GitHub:', 'white'),
          '\033[35;4mhttps://github.com/pachara1337\033[0m')
    print(colored('[Info]', 'green'), colored('Contact', 'white'), colored('thug@pachara.club', 'magenta'))
    status = 'Disabled'
    
    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = 'Enabled ' if colorant.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()

if __name__ == '__main__':
    main()
