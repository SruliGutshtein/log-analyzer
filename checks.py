from config import INTERNAL_IP, SENSITIVE_PORTS, NORMAL_SIZE, NIGHT_ACTIVITY


def is_external_ip(ip):
       """פונקציה שבודקת אם כתובת ip הוא חיצוני"""
       return not ip.startswith(INTERNAL_IP)

def is_sensitive_port(port):
       """פונקציה שבודקת אם כתובת port הוא רגיש"""
       return port in SENSITIVE_PORTS

def is_large_packet(size):
       """פונקציה שבודקת אם הגודל הוא חשוד"""
       return int(size) > NORMAL_SIZE

def is_night_activity(time):
       return int(NIGHT_ACTIVITY[0]) <= int(time) < (NIGHT_ACTIVITY[1])