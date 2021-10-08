# *
# **
# ***
# ****
# *****

size = int(input("Enter size: "))

for i in range(size):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
