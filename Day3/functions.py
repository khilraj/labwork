def login():
    print('something is wrong')
login()

def add():
    x=20
    y=15
    c= x+y
    print(c)
add()

def login(username, password):
    print(f'your username is: {username} and your password is: {password}')
login('bishal', 'battle')

def first(name):
    print('your name is', name)
first('bishal')

def add (first, second):
    ans= first+second
    print('the sum is', ans)
add(5,4)

#positional arguments
def pw (x,y):
    z= x+y
    print(z)
pw(2,8)

#same
def pw (x,y):
    z=x+y
    print(z)
pw(y=8,x=2)

#default arguments
def show (name, age=20):
    print(name,age)
show(name='bishal')

def show (name,age=12):
    print(name,age)
show(name='bishal', age= 30)

#variable length arguments
def show (*num):
    z=num[0]+num[1]+num[2]
    print(z)
show(5,4,3)

def show (*num):
    z=num[0]+num[1]+num[2]
    print(z)
show(2,5,8,7)

#keyword variable length arguments
def show (**num):
    z=num['a']+num['b']+num['c']
    print(z)
show(a=5,b=9,c=4)

def show(**num):
    z=num['a']+num['b']
    print(z)
show(a=9,b=4,c=3)

def add(x,y):
    c=x+y
    return c
sum= add(20,9)
print(sum)

