'''
Here is what we covered on Day 4, 20OCT2021
'''
'''
Code wars: 
Problem Description: Welcome. In this kata you are required to, given a string, replace every letter 
with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return 
it. a being 1, b being 2, etc. As an example:
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)
'''

def alphabet_position(text):
	ans = ''
	inp = list('abcdefghijklmnopqrstuvwxyz')
	for i in text:
		if i.isalpha():
			ans += str(inp.index(i.lower()) + 1) + ' '
	return ans[0:len(ans)-1]
#print(alphabet_position("The sunset sets at twelve o' clock."))

'''
CodeWars:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a 
function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
'''
def is_isogram(string):
    s = string.lower()
    return len(set(s)) == len(s)

'''
CodeWars:
In this kata you will create a function that takes a list of non-negative 
integers and strings and returns a new list with the strings filtered out.
'''
def filter_list(l):
    strs = list(filter(lambda elm: not isinstance(elm, str), l))
    print(strs)

'''
CodeWars:
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. if that value has more
than one digit, continue reducing in this way until a single-digit
number is prduced. The input will be a non-neg int. 
'''
def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
        print(n)
    return n

'''
SHIT THAT WILL DEF BE ON TEST!!!!!!
'''
def split_tech(str1):
    str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
    freq_words = {}
    for word in str1.split():
        if word in freq_words:
            freq_words[word] += 1
        else:
            freq_words[word] = 1
    for word in str1.split():
        freq_words[word] = freq_words.get(word,0) +1

'''
Class example
'''
def mymax(iterable):
    curmax = iterable[0]
    for item in iterable:
        if key is None:
            if item > curmax:
                curmax = item
        else:
            if key(item) > key(curmax):
                curmax = item
    return curmax
#if __name__ == '__main__':
   # l = ['AAAAAAAAAAAAAAAAAAAAAAAAA', 'c', "bbbbbbbbbbbbbbbbbb"]
   # print(mymax(l, key=len))

'''
11.12.2.6 from runestone acad. FOPP 
Create the dictionary characters that shows each character from the
string sally and its frequency. Then, find the most frequent letter 
based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for char in sally:
    characters[char] = characters.get(char,0) + 1

best_char = max(characters,key= characters.get)
print(best_char)
'''

'''
PyAct 24
Use python to produce code below that will perform the following:

A list of words is provided in the file specified by fname.
Another list of words is provided as the parameter words.
Return a list of all the words found in the file that are NOT 
contained in the list of words in parameter.
Each word in the file will be separated by at least one character of whitespace.
'''
def diffwords(fname, words):
    with open(fname) as f1:
        f_words = f1.read().split()
        comp = set(f_words) - set(words)
    print(list(comp))
#diffwords("input.txt", ['hello', 'what', 'is', 'up'])

'''
PyAct 25
def count_words(filepath):  Count the occurrences of each word in the file. 
Create a dictionary that contains each word in the file as a key and the value 
for each key will contain the number of times each words is found in the file. 
Words will be separated by one or more whitespace characters spread over multiple lines.
Args:
       filepath (str): The path to the file
   Returns:
       dict : keys - words
              values - number of times each word appears
'''
def count_words(filepath):
    text = open(filepath, "r")
    d = dict()

    for line in text:
        line = line.strip()
        words = line.split()

        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    print(d) 

'''
PyAct 26
Use python to produce code below that will perform the following:
Create a function called infinitearguments that will:
Print to standard output all positional arguments, in the order received, 
on separate lines.
Followed immediately by all keyword arguments in the form keyword=value 
in keyword alphabetic order.
'''
def infinitearguments(*a, **b):
    # b = {'z': 1, 'q': 2, ...}
    for i in a:
        print(i)
    keys = list(b.keys())  # k = ['z', 'q', 'a', 'b']
    keys.sort()            # k = ['a', 'b', 'q', 'z']
    for key in keys:
        print('{}={}'.format(key, b[key]))
#infinitearguments("Hello World","ayp",'awwas',z=1,q=2, a= 3,b= 4)
'''
PyAct 27
def sort_ascii(filepath):
Read all lines from file in filepath and return a list of all lines in case-insensitive ASCII order.
Remove all linebreaks before sorting.

  Args:
      filepath (str): The path to the file
  Returns:
      list : lines from input file sorted into ASCII order without linebreaks
'''
def sort_ascii(filepath):
    with open(filepath) as f1:
        lines = [line.strip() for line in f1.readlines()]
        print(sorted(lines, key=str.casefold))
#sort_ascii("input.txt")
'''
PyAct 28
def sort_length(filepath):
Read all lines from file in filepath and return a list of all lines sorted longest to shortest.
Remove all linebreaks before sorting.

  Args:
      filepath (str): The path to the file
  Returns:
      list : lines from input file sorted longest to shortest without linebreaks
'''
def sort_length(filepath):
     with open(filepath) as f1:
         lines = [line.strip() for line in f1.readlines()]
         return sorted(lines, key=len, reverse=True)
'''
def sort_embedded(filepath):
Read all lines from file in filepath and return a list of all lines sorted numerically by
the number at character positions 10 to 15 in each line..
Remove all linebreaks before sorting.
Example: The embedded number is 561234 below.
1         2         3         4
123456789012345678901234567890123456789012
Here is a561234 long line of text from the file.

  Args:
      filepath (str): The path to the file
  Returns:
      list : lines from input file numerically sorted on the embedded number without linebreaks
'''
def sort_embedded(filepath):
    with open(filepath) as f1:
        lines = [line.strip() for line in f1.readlines()]
    lines.sort(key = lambda l : int(l[9:14]))
    print(lines)
sort_embedded("number.txt")
'''
CodeWars 
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with 
all of the integer's divisors(except for 1 and the number itself), from smallest to largest. 
If the number is prime return the string '(integer) is prime' (null in C#) 
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
'''

