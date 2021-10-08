#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

size = int(input("Enter the size: "))

center = int(size / 2)
star_location = center
space_location = 0

for i in range(size):
    for j in range(center + 1):
        if (i < center):
            if (j >= star_location):
                print("* ", end="")
            else:
                print(" ", end="")
        elif (i == center):
            print("* ", end="")
        else:
            if (j <= space_location):
                print(" ", end="")
            else:
                print("* ", end="")

    if (i < center):
        star_location -= 1
    if (i > center):
        space_location += 1
    print("\n")
