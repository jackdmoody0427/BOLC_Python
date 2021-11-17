'''
Day 8
'''

'''
def megahertz():
    Given a dictionary (catalog) whose keys are product names and values 
    are product prices per unit and a list of tuples (order) of product names 
    and quantities, compute and return the total value of the order.
'''
def q6(catalog, order):
    total = 0
    for product, qty in order:
        price = catalog[product]
        total += price * qty 
    return total 
    
#q6({ 'AMD Ryzen 5 5600X': 289.99, 'Intel Core i9-9900K': 363.50, 'AMD Ryzen 9 5900X': 569.99 },[ ('AMD Ryzen 5 5600X', 5), ('Intel Core i9-9900K', 3)] )
'''
def 50cc_stat():
    Given an integer and limit, return a list of even multiples of the integer up to and including the limit.
    For example, if integer = 3 and limit = 30, the returned list should be [0,6,12,18,24,30]. 
    Note, 0 is a multiple of any integer except 0 itself.
'''
def q1(integer, limit):
    a = list(range(0, limit+1, integer))
    l = [i for i in a if i % 2 ==0]
    return l 
#q1(3,30)

'''
def dif_time_saves_nine():
    Given two filenames, return a list whose elements consist of line numbers for which the two files differ. 
    The first line is considered line 0
'''
def q1(f0,f1):
    with open(f0) as f0, open(f1) as f1:
        f0 = f0.readlines()
        f1 = f1.readlines()
        minim = min(len(f0), len(f1))
        maxim = max(len(f0), len(f1))
        l = []

        for i in range(minim):
            if f0[i] != f1[i]:
                l.append(i)
        for i in range(minim, maxim):
                l.append(i)
    print(l)
#q1("orphan.txt", 'out2.txt')
'''
def pass_go_collect_200():
    Given 3 scores in the range [0-100] inclusive, 
    return 'GO' if the average score is greater than 50. Otherwise return 'NOGO'.
'''
def q1(s1,s2,s3):
    l = [s1,s2,s3]
    avg = sum(l)/len(l)
    if avg > 50 and avg <=100:
        print("GO")
    elif avg > 0 and avg <= 50:
        print("NO GO")
#q1(70,70,70)

'''
def maybe_biggest_wheel():
    Given a sentence as a string with words being separated by a single space, 
    return the length of the shortest word.
'''
def q(strng):
    s = min(strng.split(), key = len)
    print(len(s))
#q("hello how are you today")

'''
def mirror_mirror():
    Given a string of multiple words separated by single spaces, 
    return a new string with the sentence reversed. The words themselves should remain as they are.
    For example, given 'it is accepted as a masterpiece on strategy', 
    the returned string should be 'strategy on masterpiece a as accepted is it'.
'''
def q1(sentence):
    words = sentence.split(' ')
    rev = ' '.join(reversed(words))
    print(rev)
#q1('it is accepted as a masterpiece on strategy')

'''
def Bring_it_together_make_it_pretty():
    Given two lists of integers, return a sorted list that contains all integers from both lists in descending order.
    For example, given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1]. The returned list may contain duplicates.
'''
def q1(lst0, lst1):
    res = sorted(lst0 + lst1, reverse = True)
    print(res)
#q1([3,4,9], [8,1,5])

'''
def is_this_the_imposter():
    Return the first duplicate value in the given list.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should be 7.
'''
def q1(lst):
    have_seen = set()
    for item in lst:
        if item in have_seen:
            print(item)
        have_seen.add(item)
#q1([5,7,9,1,3,7,9,5])

'''
def in_other_words():
    Given a list of positive integers sorted in ascending order, 
    return the first non-consecutive value. If all values are consecutive, 
    return None.
    For example, given [1,2,3,4,6,7], the returned value should be 6.
'''
def q1(arr):
    for i,j in enumerate(arr,arr[0]):
        if i!=j:
            return j
#q1([1,2,3,4,5,6,7])

'''
def Sprinkle_commas():
    Given a positive integer, return its string representation with 
    commas seperating groups of 3 digits.
    For example, given 65535 the returned string should be '65,535'.
'''
def q1(n):
    print(f'{n:,}')
#q1(65535)

'''
def There_some_chars_there():
    Given an alphanumeric string, return the character whose ascii value 
    is that of the integer represenation of all of the digits in the string 
    concatenated in the order in which they appear.

    For example, given 'hell9oworld7', the returned character 
    should be 'a' which has the ascii value of 97.
'''
def q1(strng):
    l = []
    for i in strng:
        if i.isdigit():
            l.append(i)
    s = int(''.join(l))
    s = chr(s)
    print(s)
q1('hell9oworld7')