# AdventofCode3.py

# half of string is in compartment 1, second half is in compartment 2. Each letter is one item
# lowercase items type a-z has prio 1-26, uppercase 27 to 52.

f = open("Day3.txt")
lines = f.readlines()

import string
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
prio_lowercase = range(1,27)
prio_uppercase = range(27,53)
sumPrio = 0
used_letters = []

#this get a line from the list, and splits it in half. Returns list with both halves.
def SplitString(line_from_list):
    length = len(line_from_list)
    half_length = length/2
    rugsack_one = []
    rugsack_two = []
    for i in range(length):
        if i <= half_length:
            rugsack_one.append(line_from_list[i])
        elif i > half_length:
            rugsack_two.append(line_from_list[i])
    return rugsack_one, rugsack_two

def get_prio(letter):
    if letter.islower():
        index_letter = lowercase.index(letter)
        prio = prio_lowercase[index_letter]
    elif letter.isupper():
        index_letter = uppercase.index(letter)
        prio = prio_uppercase[index_letter]
    else:
        prio = 0
    #print(prio, letter)
    return prio

"""
sumline = 0
f1, f2 = SplitString(lines[0])
test = 0
for i in f1:
    if i in f2:
        test += 1
        #f2.remove(i)
        sumline = sumline + get_prio(i)
print(sumline)

"""   


for i in lines:
    first_rugsack,second_rugsack = SplitString(i)
    used_letters = []
    for x in first_rugsack:
        if x in second_rugsack and x not in used_letters:
            sumPrio = sumPrio + get_prio(x)
            used_letters.append(x)
    print(sumPrio, first_rugsack)

   
#print(sumPrio)

        
