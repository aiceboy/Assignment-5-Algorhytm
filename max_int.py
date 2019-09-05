max_int = 0
on = True
while on == True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int >= 0:
        if num_int >= max_int:
            max_int = num_int
    else:
        break

print("The maximum is", max_int)    # Do not change this line
