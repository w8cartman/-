a=input()
while int(a[0])!=1 and len(a)<10:
    a=str(int(a[0])*int(a))
print(a)


number = int(input())
while str(number)[0] != '1' and number < 1000000000:
    number *= int(str(number)[0])
print(number)
