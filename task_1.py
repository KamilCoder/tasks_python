N=int(input('x = '))

if N >=0 :
	N_Reverse=int(str(N)[::-1])
else:
	N_Reverse=-(int(str(abs(N))[::-1]))
	#przeksztalcamy N w liczbe dodatnia
	#konwertujemy na string aby moc odwrocic kolejnosc
	#przeksztalcamy na ujemny int aby wynik 
	#nie byl stringiem.

if (N_Reverse >= -2147483649) and (N_Reverse <= 2147483647):
	print(N_Reverse)
else:
	print('0')
