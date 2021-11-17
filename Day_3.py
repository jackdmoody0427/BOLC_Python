#This Begins Day 3 of Python
'''
Exercise PyAct 11
Print out every even number on a separate line from parameters first to last, inclusive.
Next print out every odd number from first to last, inclusive.
'''
def evensandodds(first, last):
    for num in range(first, last +1):
        if num %2 ==0:
            print(num)
    for num in range(first, last +1):
        if num%2!=0:
            print(num)

#evensandodds(1,10)

'''
PyAct 12
def user_io():

     Returns a list of items read from the user until the user enters an empty string.

     Args:
         None
     Returns:
         list: a list of strings 
 pass
 
'''
def user_io():
    lst = []
    while True:
        inp = input("please enter inputs till you want to put in an empty str: ")
        if inp == '':
            break
        else:
            lst.append(inp)
    return(lst)
#user_io()

'''
PyAct 13-1 
def make_tuple(a,b):
       Returns a tuple of the multiples of 10 from a to b inclusive.
       Args:
           None
       Returns:
           tuple: a tuple of the multiples of 10 from a to b inclusive

PyAct 13
 def make_tuple():
     Returns a tuple of the multiples of 10 from 1 to 100 inclusive.
     Args:
         None
     Returns:
         tuple: a tuple of the multiples of 10 from 1 to 100 inclusive  
#or some other preprocessing
    for num in range(1,101):
        if num %10 ==0:
            lst.append(num)
    x = tuple(lst)
    print(lst)
    return tuple(lst)
'''

'''
PyAct 14
 def strings():
    
     Returns a tuple of the following strings:

     (empty string)#or some other preprocessingse's operating system

     Args:
         None
     Returns:
         tuple: a tuple of strings
'''
def strings():
    return ('', 'Physics is the universe\'s operating system')

'''
PyAct 15
 def disect(lst):
     Returns a tuple of the given list split into two equally sized halves.
     The given list will always consist of an even number of elements.
     Args:
         lst (lst): a list of elements
     Returns:
         tuple: a tuple of two lists
'''    
def disect(lst):
    if len(lst)%2 ==0:
        half = len(lst)//2
        first_h = lst[:half]
        second_h = lst[half:]
        return (first_h, second_h)

'''
 PyAct 16
  def reverse_string(strng):
     Returns a copy of the given string reversed
     Args:
         strng (str): a string of alphanumeric characters
     Returns:
         str: a copy of the given string reversed
'''
def reverse_string(strng):
    for num in range(a,b):
        return strng[::-1]

'''
PyAct 17
 def code_points(strng):
     Returns a list of ordinals for every character in the given string
     Args:
         strng (str): a string of alphanumeric characters
     Returns:
         list: ordinals of every character in the given string
'''
def code_points(strng):
    lst = []
    for char in range(0, len(strng)):
        lst.append(ord(strng[char]))
    print(lst)#or some other preprocessing
    return lst 


'''
PyAct 18
Read file specified by the path in inpath parameter and write all lines to the file specified
by the outpath parameter.
Before writing out each line, add the line number starting with 1 follow by colon and space.
def linenums(inpath, outpath): pass
'''
def linenums(inpath, outpath):
    lines = []
    with open(inpath, 'r') as file:
        for count, line in enumerate(file.readlines()): 
            line = line.strip() 
            lines.append('%-1d: %s' % (count + 1, line)) 
    with open(outpath, 'w') as file:
        file.write("\n".join(lines))
#linenums("input.txt", "output.txt")

'''
PyAct 19
def grab(lst):
     Returns a randomly chosen item from the given list (lst).
     Args:
         lst (list): a list of items
     Returns:
         item (?): an item from the list
'''
def grab(lst):
    import random
    print(random.choice(lst))

'''
pyAct 20
def get_hash(data="python"): Returns the SHA3 256-bit hash of the data provided. 
You will need to use the hashlib python library to complete this challenge.
   NOTE: The first call will use the string "python" later calls will use random strings
   NOTE: You can convert a string into a bytes-like object which is needed for hashing with: 
         
         <code> data.encode("utf-8") </code>
   NOTE: You can create a bytes-like object out of a literal by adding a b in front of the string, 
   ie b"python" or b'python'
   
   Args:
       data (str): data to be encoded
   Returns:
       str : The SHA3 256-bit hash of the provided data
'''
def get_hash(data='python'):
    import hashlib
    encoded_str = data.encode("utf-8")
    print(hashlib.sha3_256(encoded_str).hexdigest())

'''
PyAct 21
Write a script that implements a function, find_product, which takes two numbers 
and returns the product. Use the name=='main' idiom to prompt the user for two 
integers a print the result of calling find_product using those integers.

def find_product(a,b):
    return a*b
if __name__ == "__main__":

    a = int(input("put a in: "))
    b = int(input("put b in: "))
    print(find_product(a,b))
'''

'''
PyAct 22
Write a function, round_to_position, which takes a list of floats and returns 
a new list with the original floats each rounded to the number of digits of 
precision after the decimal point corresponding to the original float's position in the list.
'''
def round_to_position(lst):
    n_list = []
    for i,num in enumerate(lst):
        r = round(num,i)
        n_list.append(r)
    return n_list
    print(n_list)
#round_to_position([20.5,23.2,20.1,22.5555555555,23.1])

'''
PyAct 23
def get_type_str(obj): Returns the type of the parameter as a string. Possible types are:
string
boolean
integer
float
list
tuple
NOTE: Any other types should be identified with 'unknown'
'''
def get_type_str(obj):
    if 'str' == type(obj).__name__:
        return "string"
    elif 'bool' == type(obj).__name__:
        return "boolean"
    elif 'int' == type(obj).__name__:
        return "integer"
    elif 'float' == type(obj).__name__:
        return "float"
    elif 'list' == type(obj).__name__:
        return "list"
    elif 'tuple' == type(obj).__name__:
        return "tuple"
    else:
        return "unknown"