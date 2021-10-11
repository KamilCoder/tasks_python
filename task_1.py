def reverser():
    N = int(input('x = '))
    N_Reverse = int()
    if N >= 0:
        N_Reverse = int(str(N)[::-1])
    else:
        N_Reverse = -(int(str(abs(N))[::-1]))
     # N to positive number
     # convert to string to make reverse

    if (N_Reverse >= -2147483649) and (N_Reverse <= 2147483647):
        print(N_Reverse)
    else:
        print('0')
    # This is simpe if reverse number is smaller  or bigger than
    # signed integer range function returns
if __name__ == "__main__":
    reverser()
