def main():
    print("What time is it? ", end="")
    time = convert(input())
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
def convert(time):
    h,m = map(int, time.split(":"))
    return h + m/60
if __name__ == "__main__":
    main()