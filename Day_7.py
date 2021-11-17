'''
Here is what we did on day 7 of python
'''
'''
def its_the_end_that_is_important():
    Given a list (lst) and a number of items (n), 
    return a new list containing the last n entries in lst.
    def q1(lst,n):
        pass
 '''
def q1(lst, n):
    print(lst[-n:])
#q1([1,2,3,4,5],4)

'''
def Let_us_memorialize_this_todo_list():
    1. Given a filename and a list, 
    
    2. write each entry from the list to the file on separate 
    lines until a case-insensitive entry of "stop" is found in the list. 
    
    3. If "stop" is not found in the list, write the entire list 
    to the file on separate lines.
    
    def q1(filename, lst):
        pass
'''
def q1(filename, lst):
    with open(filename, 'w') as f:
        for word in lst: 
            if word != "stop":
                f.write(word + '\n')
            else:
                break

#q1("out2.txt", ["hi","yellow",'sup','ah','mp', 'die'])

'''
def Alexa_how_long_is_the_first_line():
    Given a filename, open the file and 
    return the length of the first line in the file 
    excluding the line terminator.

    def q1(filename):
        pass
'''
def q1(filename):
    with open(filename) as f1:
       f = f1.read().splitlines()
       #f = f.replace('\n','')
       print(len(f[0]))
#q1("orphan.txt")
'''
def Greeting_of_the_day():
    Given the military time in the argument miltime, 
    return a string containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
'''
def q1(miltime):

    if miltime >= 300 and miltime < 1200:
        print("Good Morning")
    if miltime >= 1201 and miltime < 1600:
        print("Good Afternoon")
    if miltime >= 1601 and miltime < 2059:
        print("Good Evening")
    if miltime >= 2100 and miltime < 259:
        print("Good Night")

'''
def This is the socket block():
'''

'''
def Put_into_number():
    Given an input string, return a list containing the ordinal 
    numbers of each character in the string in the order found 
    in the input string.
'''
def q1(string):

    return [ord(x) for x in list(string)]

'''
def better_than_avg():
    Given the variable length argument list, return the 
    average of all the arguments as a float
'''
def q1(*args):
    avg = float(sum(args)) / len(args)
    #return avg
    print(avg)

#q1(1,2,3,4,5)

'''
def Say_slower():
    Given an input string, return a tuple with each element 
    in the tuple containing a single word from the input 
    string in order.
'''
def q1(strng):
    print(tuple(strng.split()))

'''
def Why_so_negative():
    Given the argument numlist as a list of numbers, 
    return True if all numbers in the list are NOT negative. 
    If any numbers in the list are negative, return False.
'''
def q1(numlist):
    for i in numlist:
        if i < 0:
            print(False)
    print(True)

'''
def megahertz():
    Given a dictionary (catalog) whose keys are product names and values 
    are product prices per unit and a list of tuples (order) of product names 
    and quantities, compute and return the total value of the order.
'''
def q6(catalog, order):
    for i in order:
        quant = order[1]
        print(i)
q6({ 'AMD Ryzen 5 5600X': 289.99, 'Intel Core i9-9900K': 363.50, 'AMD Ryzen 9 5900X': 569.99 },[ ('AMD Ryzen 5 5600X', 5), ('Intel Core i9-9900K', 3)] )


'''
float_your_boat:
 Given the floatstr, which is a comma separated string of floats
 r a list with each of the floats in the argument as elements in the list.
'''

def q1(floatstr):
    g = floatstr.split(",")
    k = [float(i) for i in g]
    print(k)
#q1("9.0,2.3,3.4")

'''
def card_class():

    import random
    from collections import deque

    class Card:

        SPADE = '\u2660'
        HEART = '\u2665'
        DIAMOND = '\u2666'
        CLUB = '\u2663'

        def __init__(self,rank,suit):
            self.rank = rank
            self.suit = suit

        def __str__(self):
            return '{}{}'.format(self.rank,self.suit)

        def __repr__(self):
            return str(self)


    class Deck:

        def __init__(self):
            self.cards = deque()
            for suit in [Card.SPADE,Card.HEART,Card.DIAMOND,Card.CLUB]:
                for rank in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']:
                    self.cards.append( Card(rank,suit) )

        def shuffle(self):
            random.shuffle(self.cards)

        def deal(self,cards=1):
            return [self.cards.popleft() for _ in range(cards)]


    if __name__ == '__main__':
        deck = Deck()
        deck.shuffle()
        hand = deck.deal(5)
        print(hand)
'''
