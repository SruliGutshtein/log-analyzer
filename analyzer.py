from checks import is_external_ip, is_sensitive_port, is_large_size


def identifying_suspicions_ips(packets):
    """פונקציה שעוברת על רשימה וממיינת את הips חיצוניים לרשימה חדשה"""
    external_ips = [packet[1] for packet in packets if is_external_ip(packet[1])]
    return external_ips

def identifying_suspicions_ports(packets):
    """פונקציה שעוברת על רשימה וממיינת את הפורטים הרגישים לרשימה חדשה"""
    sensitive_port = [packet for packet in packets if is_sensitive_port(packet[3])]
    return sensitive_port

def identifying_large_sizes(packets):
    """פונקציה שעוברת על רשימה וממיינת את אלו עם גודל חשוד לרשימה חדשה"""
    large_size = [packet for packet in packets if is_large_size(packet[-1])]
    return large_size