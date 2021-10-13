def reverser():
    N = int(input('x = '))
    N_Reverse = int()
    if N >= 0:
        N_Reverse = int(str(N)[::-1])
    else:
        N_Reverse = -(int(str(abs(N))[::-1]))

    if -2147483649 <= N_Reverse <= 2147483647 :
        return(N_Reverse)
    else:
        return('0')
    
if __name__ == "__main__":
    reverser()
