from checks import is_external_ip, is_sensitive_port, is_large_packet, is_night_activity


def identifying_suspicions_ips(packets):
    """פונקציה שעוברת על רשימה וממיינת את הips חיצוניים לרשימה חדשה"""
    return [packet[1] for packet in packets if is_external_ip(packet[1])]

def identifying_suspicions_ports(packets):
    """פונקציה שעוברת על רשימה וממיינת את הפורטים הרגישים לרשימה חדשה"""
    return [packet for packet in packets if is_sensitive_port(packet[3])]

def identifying_large_sizes(packets):
    """פונקציה שעוברת על רשימה וממיינת את אלו עם גודל חשוד לרשימה חדשה"""
    return [packet for packet in packets if is_large_packet(packet[-1])]

def add_size_tag(packets):
    """פונקציה שעוברת על רשימה ועושה רשימה חדששה עם תיוג אם הגודל חשוד"""
    return [packet + ["LARGE"] if is_large_packet(packet[-1]) else packet + ["NORMAL"] for packet in packets]

def identifying_night_activity(packets):
    """פונקציה שעוברת על רשימה וממיינת את אלו עם שעת פעילות חשודה לרשימה חדשה"""
    return  [packet for packet in packets if is_night_activity(packet[0][-8:-6])]

def counting_requests_by_ip(packets):
    """פונקציה שמקבלת את הנתונים ומחזירה מילון: כתובת IP מקור ומספר הפניות שלה"""
    list_ip = [x[1] for x in packets]
    return {k: list_ip.count(k) for k in {packet[1] for packet in packets}}

def port_to_protocol_mapping(packets):
    """פונקציה שמקבלת את הנתונים ומחזירה מילון: מספר פורט ושם הפרוטוקול"""
    return {port[3]: port[4] for port in packets}

def ip_suspicion_details(packets):
    """פונקצייה שמחזירה מילון שבו המפתח הוא IP
    והערך הוא רשימה של כל החשדות שנמצאו לגביו"""
    set_ips = {packet[1] for packet in packets}
    return {ip: list({suspicion for packet in packets
            if packet[1] == ip
            for suspicion in ((["EXTERNAL_IP"] if is_external_ip(packet[1]) else [])
                + (["SENSITIVE_PORT"] if is_sensitive_port(packet[3]) else [])
                + (["LARGE_PACKET"] if is_large_packet(packet[-1]) else [])
                + (["NIGHT_ACTIVITY"] if is_night_activity(packet[0][-8:-6]) else []))})
        for ip in set_ips}