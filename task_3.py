import math
words = str(input('words = '))
maximum_width = int(input('maximum_width = '))
words_list = []
words_separated = words.split()
temp = str()

if maximum_width <= (len(max(words_separated,key=len))):
    print('maximum_width must have biger value than longest word')
    #podana dlugosc musi byc wieksza niz najdluzsze slowo
else:
    
    for word in words_separated:

        if len(word) == maximum_width:
            words_list.append(temp)
            words_list.append(word)
            temp = str()
        elif (len(temp)+len(word)) == maximum_width:
            words_list.append(temp+word)
            temp = str()
        elif (len(temp)+len(word)) < maximum_width:
            temp += (word+" ")
        elif (len(temp)+len(word)) > maximum_width:
            words_list.append(temp)
            temp = word+" "
        
    if temp:
        words_list.append(temp[0:(len(temp)-1)]) 
    #ostatnie slowo jesli jest

    for i in range(len(words_list)-1):
        if (words_list[i][(len(words_list[i]))-1:]).isspace():
            words_list[i] = words_list[i][:(len(words_list[i])-1)]
    #pozbywamy sie spacji na koncu elementow listy
    #ktorymi to spacjami rozdzielalismy slowa

    for i in range(len(words_list)-1):
        if len(words_list[i]) < maximum_width:
            spaces = maximum_width-len(words_list[i])
            places = len(words_list[i].split())-1
            if places == 0:
                words_list[i]=words_list[i][0:]+(spaces*' ')
                continue
            elif spaces%places == 0:
                space_generator = str(' '*(int(spaces/places)+1))
                words_list[i] = space_generator.join(words_list[i].split())
            elif spaces%places == 1:
                space_generator = str(' '*(int(math.floor(spaces/places))+1))
                words_list[i] = space_generator.join(words_list[i].split())
                for letter in range(len(words_list[i])):
                    if words_list[i][letter].isspace():
                        words_list[i] = words_list[i][:letter]+' '+words_list[i][letter:]
                        break
    #rozstawiamy spacje
    print(words_list)

#nie dodawalem \n - nowej lini do wyniku
#bo wtedy wynik pojawia sie bez [] i ""
#nie zamienialem tez '!' na '.' 
#jak w inpucie i outpucie w pdf