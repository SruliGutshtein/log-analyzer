from config import INTERNAL_IP


def is_external_ip(ip):
       """פונקציה שבודקת אם כתובת ip הוא חיצוני"""
       return not ip.startswith(INTERNAL_IP)

