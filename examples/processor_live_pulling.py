import os
import platform

from modules.processor import ELTProcessor


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def main():
    elt808d = ELTProcessor("192.168.3.110", 50000, 18, 18, 8)
    elt808d.pull_channels()
    for i in elt808d.input_channels:
        print(i)


if __name__ == '__main__':
    while True:
        clear()
        main()
