def load_file(filepath):
    """פונקציה שמקבלת נתיב לקובץ CSV ומחזירה רשימה של רשימות - כל שורה כרשימה של שדות"""
    try:
        with open(filepath, encoding="utf-8") as f:
            n_list = []
            for line in f:
                n_list.append(line.strip().split(","))
        return n_list
    except Exception as e:
        print(e)
        return e