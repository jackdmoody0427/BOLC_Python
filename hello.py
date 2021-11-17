#!usr/bin/env python3

print("Hello all")
print("ahhhhhh")

for x in range (1,6):
    print(x+1)


pie_size = 3.14

print(type(pie_size))

int_input = "3.1415"

print(float(int_input))


sentence = 'good for all'

sent_list = sentence.split()
print(sent_list)

sent_list[0] = "f"

sent_list[-1] = "?"

print(sent_list)

sent_list2 = '.'.join(sent_list)

print(sent_list2)

nums = "1 2 3 4" 

nums2 = nums.split()
nums2 = "+".join(nums2)
print(nums2)

inp =int(input("Enter an integer: "))

if inp == 0:
    print("Zero")
else:
    if inp > 0:
        print("Positive", end = " ")
    else:
        print("Negative", end = " " )
    if inp % 2 ==0:
        print("Even")
    else:
        print("Odd")

inp2 = int(input("enter an integer: "))

if inp2 % 3 and inp2 % 5:
    print(inp2)
else:
    if inp2 %3 ==0 and inp2 %5 ==0:
        print("fizzbuzz")
    elif inp2 %5 ==0:
        print('buzz')
    elif inp2 %3 ==0:
        print("fizz")
