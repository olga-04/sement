print('Hva er målene til gulvet du skal støpe? Oppgi dem i meter')
var1 = input('Husk komma mellom hvert tall: ')
var2 = (var1.split(","))
print(var2)

a = (float(var2[0]) * float(var2[1]) * float(var2[2]))

print('Dette er hvor mange kubikkmeter sement du skal fylle med sement: ' + str(a))

b = (float(a) / 0.001)
c = "{:.2f}".format(a)

print('Du trenger: ' + (c) + ' liter med sement')