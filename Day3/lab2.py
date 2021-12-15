m1 = int(input('enter the marks of first subject: '))
m2= int(input('enter the marks of second subject: '))
m3= int(input('enter the marks of third subject: '))
m4= int(input('enter the marks of fourth subject: '))
total_marks= m1+m2+m3+m4
print(total_marks)
percentage = (total_marks/100)
if m1>85 and percentage>=100:
    print(f'congrats! you got A grade')
elif m2>60 and percentage<=100:
    print(f'congrats! you got B+ grade')
elif m3>45 and percentage>=100:
    print(f'you are just pass')
else:
    print(f'sorry! you are fail ')