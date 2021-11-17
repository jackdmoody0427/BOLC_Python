'''
Day 9
'''

'''
There will be no need to import modules outside of socket unless you want to
'''
def char_num_convert():
    strng = 'he9l7o'
    digits = []
    for char in strng:
        if char.isdigit():
            digits.append(char)
    print(digits)

    alpha = []
    for char in strng:
        if char.isalpha():
            alpha.append(char)
    print(alpha)
#char_num_convert()

'''
convert ipv4 address into numbers. 
you should split it on the periods
then convert to integers
'''
def ip_check():
    ip = '192.168.0.10'
    octet = ip.split('.')
    print(octet)
    if int(octet[0]) > 191:
        print(True)
#ip_check()
def dict_ex():
    d = {'key0':'val0','key1':'val1'}
    for item in d:
        print(item)
    for item in d.values():
        print(item)
    for key,value in d.items():
        print(key, value)

def ranges():
    a = list(range(10))
    b = list(range(2,10))
    c = list(range(2,10,2))
    d = list(range(1,10,-1))
    print(a,'\n',b,'\n',c, d)
#ranges()

'''
with open('test.txt') as src, open('test2.txt',w) as dst:
learn how to advance through multiple files at the same time

####################################
#           *args = tuple
#           **kwargs = dictionary
####################################
'''
def sort_list():
    #in order to hand lists for sorting
    s = ["1","2","55","100"]
    print(sorted(s))
    print(sorted(s,key=len))
    q = [int(x) for x in s]
    print(sorted(q,reverse=True))
#sort_list()
import socket
def q16(host, port):
    # we will use tcp over ipv4 client 
    s = socket.socket()
    s.connect((host.port))
    data = s.recv(4096)
    return data 

#codewars
def high_and_low(numbers):
    n = numbers.split(" ")
    mx = max(n)
    mn = min(n)
    mx = str(mx)
    mn = str(mn)
    return mx +  ' ' + mn
    return "{} {}".format(mx, mn)
#high_and_low("1 2 3 4 5")

#codewars
def accum(s):
    #accum("abcd") -> "A-Bb-Ccc-Dddd"
    output = []
    for count, letter in enumerate(s):
        output.append(letter.upper() + letter.lower()*(count))
    print('-'.join(output))
    return '-'.join(output)
accum("abcd")

#codewars
def get_count(sentence):
    s = sentence.split()
    