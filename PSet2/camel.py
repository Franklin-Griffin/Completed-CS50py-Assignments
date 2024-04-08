print("camelCase: ", end="")
x = input()
ans = ""
for i in x:
    if i.lower() == i:
        ans += i
    else:
        ans += "_" + i.lower()
print("snake_case: " + ans)