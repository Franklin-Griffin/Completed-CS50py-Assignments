x = 50
while x > 0:
    print(f"Amount Due: {x}")
    print("Insert Coin: ", end="")
    coin = int(input())
    if coin in [5,10,25]:
        x -= coin
print(f"Change Owed: {-x}")