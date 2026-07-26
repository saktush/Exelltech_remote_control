import time
from modules.api import ASCII
from modules.system import UDP
import ipaddress as ip

local_ip = ip.ip_address("192.168.3.100")
local_port = 50000
dest_ip = ip.ip_address("192.168.3.110")
dest_port = 50000
speed = 0.01

while True:
    for i in range(18):
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.input.mute(i, 1))
        time.sleep(speed)
        # print(res)
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.input.gain(i, 0-i*4 if i < 8 else -60+i*4))
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.output.gain(i, 0-i*4 if i < 8 else -60+i*4))
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.mixer.switch(i, i, 1))
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.mixer.switch(i, 17-i, 1))
        time.sleep(speed)
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.output.mute(i, 1))
        print(res)
    time.sleep(speed)
    for i in range(18):
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.input.mute(i, 0))
        time.sleep(speed)
        # print(res)
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.input.gain(i, 0))
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.output.gain(i, 0))
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.mixer.switch(i, i, 0))
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.mixer.switch(i, 17-i, 0))
        time.sleep(speed)
        res = UDP.send(local_ip, local_port, dest_ip, dest_port, ASCII.set.output.mute(i, 0))
        print(res)

