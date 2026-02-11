from config import INTERNAL_IP, SENSITIVE_PORTS


def is_external_ip(ip):
       """פונקציה שבודקת אם כתובת ip הוא חיצוני"""
       return not ip.startswith(INTERNAL_IP)

def is_sensitive_port(port):
       """פונקציה שבודקת אם כתובת port הוא רגיש"""
       return port in SENSITIVE_PORTS