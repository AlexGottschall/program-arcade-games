#
n = int(input("n = "))
print("o" * (n*2))
for x in range((n) - 2):
    print("o", end = "")
    for y in range((n*2)-2):
        print(" ", end = "")
    print("o", end = "")
    print()
print("o" * (n*2))