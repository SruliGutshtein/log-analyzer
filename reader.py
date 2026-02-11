def load_file(filepath):
    """פונקציה שמקבלת נתיב לקובץ CSV ומחזירה רשימה של רשימות - כל שורה כרשימה של שדות"""
    with open(filepath, encoding="utf-8") as f:
        n_list = []
        for line in f:
            n_list.append(line.strip().split(","))
    return n_list

file = r"C:\Users\User\Desktop\kodkod\python\progects python\פרויקט - log analyzer\network_traffic.log"
print(load_file(file))