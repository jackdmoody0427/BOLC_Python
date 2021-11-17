'''
Here is what we/ I did for Day 5 of python
'''

'''
PyAct 100
def complexity():
    pass
    Given a password as a string, return an integer whose bits
    are set according to the following rules:

    0x1 - Consists of at least 15 characters
    0x2 - Consists of at least 1 number
    0x4 - Consists of at least 1 uppercase letter
    0x8 - Consists of at least 1 lowercase letter
    0x10 - Consists of at least 1 special character (~!"@#$%^&'*_-+=`|(){}[]:;<>,.?/)
    Note: The set of special characters corresponds exactly 
    with those characters in string.punctuation
'''
import string 

def complexity(password):
    #password = str(input("please input password of choice: "))
    bits = [0]*32
    at_least_15 = len(password) >= 15
    num_in_pass = True in [c.isdigit() for c in password]
    special_char_in_pass = True in [c in string.punctuation for c in password]
    upper = True in [c.isupper() for c in password]
    lower = True in [c.islower() for c in password]
    bits[31] = int(at_least_15)
    bits[30] = int(num_in_pass)
    bits[28] = int(upper)
    bits[24] = int(lower)
    bits[22] = int(special_char_in_pass)
    st = [str(c) for c in bits]
    a_s = "".join(st)
    print(a_s)
    a = int(a_s, 2)
    print(a)
    return a
#complexity("HellohowAreYo0!!!!!")

'''
PyAct 101
def ahhh():
    Given a linux file mode (permissions) as an integer, return the permission string that the mode represents.

 
 Example 1:
 mode = 511 
 511 == 0b111111111
 permissons = 'rwxrwxrwx'

 Example 2:
 mode = 424
 424 == 0b110101000
 permissions = 'rw-r-x---'
 '''
def perms(seq):

    result = ''
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    for digit in [int(n) for n in format(seq,"03o")]:
        for value, letter in value_letters:
            if digit >= value:
                 result += letter
                 digit -= value
            else:
                result += '-'
    return result 
'''
PyAct 102
def ahh():
    Given a username as a string, crack the user's 4 digit pin by repeatedly 
    calling the provided login function. Incorrect attempts to login will raise 
    PermissionError so this, and only this, exception must be caught. 
    Return the pin used to successfully log in.
    login(username,pin)
    
    Returns True if the username and pin are correct. Otherwise raises PermissionError.
    def crack(username):
        pass
'''
def crack(username):
    for i in range(10000):
        pin = str(i)
        try:
            if login(username,pin):
                return pin 
        except PermissionError:
            continue 

'''
PyAct 103
def tictactoe():
    Implement a class called TicTacToe
    init should not take additional arguments and should be used to initialize 
    the internal state of a game. move should only take a row and col (row 0 
    and column 0 indicate the upper left corner of the board) and return a value 
    as indicated below.
class TicTacToe:

     def __init__(self):
         pass

     def move(self,row,col):
         # Return 1 as an int if player 1 wins as a result of this move
         # Return 2 as an int if player 2 wins as a result of this move
         # Return 0 as an int if a draw results from this move
         # Return None if nothing results from this move
         # Raise an Exception for invalid moves
         pass  
'''
def tictactoe():
    pass 
class TicTacToe:
    def __init__(self):
        pass
    def move(self, row, col):
        