# utils.py
import os
import time

def limpar_terminal():
    # Para Windows
    time.sleep(3)
    if os.name == 'nt':
        os.system('cls')

