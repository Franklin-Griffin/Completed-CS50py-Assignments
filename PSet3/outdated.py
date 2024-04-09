months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        print("Date: ", end="")
        date = input()
        if "/" in date:
            x = date.split("/")
            if len(x) != 3:
                continue
            y,m,d = str(int(date[2])), str(int(date[0])), str(int(date[1]))
            print(f"{y.zfill(4)}-{m.zfill(2)}-{d.zfill(2)}")
        else:
            x = date.split(" ")
            if len(x) != 3:
                continue
            y,m,d = date[2], str(months.index(date[0]) + 1), date[1][:-1]
            print(f"{y.zfill(4)}-{m.zfill(2)}-{d.zfill(2)}")
        break
    except Exception:
        continue