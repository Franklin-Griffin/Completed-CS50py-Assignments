def main():
    print("Input: ", end="")
    x = input()
    x = shorten(x)
    print(f"Output: {x}")
def shorten(word):
    out = ""
    for i in word:
        if not i.lower() in "aeiou":
            out += i
    return out
if __name__ == "__main__":
    main()