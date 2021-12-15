a= int(input('enter a integer: '))
b= int(input('enter a integer: '))
c= int(input('enter a integer: '))
if a<b and a<c:
    print(f'a is the smallest one')
elif b<a and b<c:
    print(f'b is the smallest one')
else:
    print(f'c is the smallest one')