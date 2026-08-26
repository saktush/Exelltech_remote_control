import ipaddress as ip
import os

from dotenv import load_dotenv

load_dotenv()

LOCAL_IP = ip.ip_address(os.environ.get("EXELLTECH_LOCAL_IP", "192.168.1.100"))
LOCAL_PORT = int(os.environ.get("EXELLTECH_LOCAL_PORT", "50000"))
REMOTE_IP = ip.ip_address(os.environ.get("EXELLTECH_REMOTE_IP", "192.168.1.200"))
REMOTE_PORT = int(os.environ.get("EXELLTECH_REMOTE_PORT", "50000"))
