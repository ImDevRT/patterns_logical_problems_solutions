#     *
#    **
#   ***
#  ****
# *****

size = int(input("Enter number of rows: "))
spaces = size - 1

for i in range(size):
    for j in range(size):
        if j < spaces:
            print(" ", end="")
        else:
            print("*", end="")
    spaces -= 1
    print("\n")
