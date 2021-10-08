#     *
#    * *
#   * * *
#  * * * *
# * * * * *

size = int(input("Enter size: "))
spaces = size - 1

for i in range(size):
    for j in range(size):
        if (j < spaces):
            print(" ", end="")
        else:
            print("* ", end="")
    print("\n")
    spaces -= 1
