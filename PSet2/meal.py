def main():
    print("What time is it? ", end="")
    convert(input())
def convert(time):
    h,m = map(int, time().split(":"))
    if h == 7 or (h == 8 and m == 0):
        print("breakfast time")
    if h == 12 or (h == 13 and m == 0):
        print("lunch time")
    if h == 18 or (h == 19 and m == 0):
        print("dinner time")
if __name__ == "__main__":
    main()