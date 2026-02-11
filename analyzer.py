from checks import is_external_ip


def identifying_suspicions_ips(packets):
    """פונקציה שעוברת על רשימה וממיינת את הips חיצוניים לרשימה חדשה"""
    external_ips = [packet[1] for packet in packets if is_external_ip(packet[1])]
    return external_ips