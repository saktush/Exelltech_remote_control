import os
import platform

from _env import LOCAL_IP, LOCAL_PORT, REMOTE_IP, REMOTE_PORT
from exelltech_remote_control.processor import ELTProcessor


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    elt808d = ELTProcessor(REMOTE_IP, REMOTE_PORT, 18, 18, 8, local_ip=LOCAL_IP, local_port=LOCAL_PORT)
    elt808d.pull_channels()
    for i in elt808d.input_channels:
        print(i)


if __name__ == "__main__":
    while True:
        clear()
        main()
