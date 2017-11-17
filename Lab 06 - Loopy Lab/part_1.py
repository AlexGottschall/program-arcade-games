#
numb = 10
for row in range(9):
    for col in range(row + 1):
        print(numb, end = " ")
        numb = numb + 1
    print()