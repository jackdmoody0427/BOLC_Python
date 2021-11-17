'''
This is the beginning of Day 2 of python. 
We are covering functions and more flow control related
Topics today
'''

#making your first function
def mpg():
    a = 4
    print(a)

#You call a function by writing it's name then ()
#mpg()

def someotherfun():
    pass

#It is best practice to have all funcs at the top, then call at the end
#mpg()
#someotherfun()

'''
Recall that functions and variables inside them have scope, 
So these create areas of isolation so that problems within
those functions are localized and don't interfere with outside
functions and variables, unless specified otherwise
'''

#just fucking around
def duh():
    for i in range(1,10):
        x= i + 1
        print (x)
    pass

#duh()

#exercise PyAct09

def reverseit():
    lst = []
    while True:
        line = input()
        lst.append(line[::-1])
        if line == '':
            break
    print('\n', lst[0:len(lst)-1])

def domath(a,b,c):
    d = (a + b)*c
    return d

#Exercise Gues Number
def guess_number(n):
    while True:
        x =  int(input("put in num now: "))
        if x > n:
            print("Too High")
        elif x < n:
            print("Too Low")
        else:
            print("WIN")
            return 

#guess_number(23)

#PyAct 10
def leetString(s):
    lst = []
    for index in range(len(s)):
        if index %2 ==0:
            lst.append(s[index].upper())
        else:
            lst.append(s[index].lower())
    print(''.join(lst))

leetString("helloworld")
