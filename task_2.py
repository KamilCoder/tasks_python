def dialer():
    phone = {
            1:[],
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']}
        #dictionary phone as model
        #simulating phones keyboard

    output=[]
    digitsList=[]
    digits=abs(int(input('digits = ')))
    #Using abs() to convert numbers to positive

    if not digits:
        print(output)
    else:
        for digit in str(digits):
            digitsList.append(int(digit))
        
        if len(str(digits)) > 1:
            for fl in phone[digitsList[0]]:
                for sl in phone[digitsList[1]]:
                    output.append(fl+sl)        
            print(output)
        else:
            print(phone[int(digits)])

#Like in your task I assume that user
#want to check combinations of 2 numbers

if __name__ == "__main__":
    dialer()