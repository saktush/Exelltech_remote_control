import ipaddress as ip

LOCAL_IP: ip.IPv4Address = ip.ip_address("192.168.3.100")
LOCAL_PORT: int = 50000

REMOTE_IP: ip.IPv4Address = ip.ip_address("192.168.3.185")
REMOTE_PORT: int = 50000
