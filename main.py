from math import *

a = 10
b = 5
c = 2

dzielenie = b/c
print(dzielenie)
dzielenie_calkowite = b // c
print(dzielenie_calkowite)

dodawanie = a+b
potega = a ** c
print(dodawanie)
print(potega)

potega = pow(b,c)
print(potega)

print(sqrt(9))

print(pi)

imie = "Radek"
wiek = 27

print("mam na imie %s i mam %d lat" % (imie, wiek))

print("wynik dzialania jest rowny a=%(zm)d" % {'zm':12})

x = 5
y = 3
z = 5-3
print("wynik dzialania %(z1)d-%(z2)d=%(z3)d" % {'z1':x, 'z2':y, 'z3':z})