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
        #tworzymy slownik, jako wzor
        #przyjmujac klawiature telefonu

output=[]
digitsList=[]
digits=abs(int(input('digits = ')))
#dzieki abs() eliminujemy minus

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

#zalozylem ze jak w zadaniu uzytkownik 
#chce uzyskac kombinacje z dwoch cyfr
