def swap(str):
    start=str[0]
    end=str[-1]
    swap=end+str[1:-1]+start
    print("The string is:",str)
    print("The swapped string is:",swap)
swap("pumpkin")
