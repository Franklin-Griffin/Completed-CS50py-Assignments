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
            y,m,d = str(int(x[2])), str(int(x[0])), str(int(x[1]))
            if int(d) > 31:
                continue
            print(f"{y.zfill(4)}-{m.zfill(2)}-{d.zfill(2)}")
        else:
            x = date.split(" ")
            if len(x) != 3:
                continue
            if not "," in x[1]:
                continue
            y,m,d = x[2], str(months.index(x[0]) + 1), x[1][:-1]
            if int(d) > 31:
                continue
            print(f"{y.zfill(4)}-{m.zfill(2)}-{d.zfill(2)}")
        break
    except Exception:
        continue