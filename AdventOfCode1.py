
# list for calories per elf
elves = []
# sum of calories
calories = 0
#sum of calories of top 3 elves
topElves = 0

#read file
with open('/../inputday1.txt') as f:
    lines = f.readlines()

# goes through file and adds calories per elf
for i in lines:
    if i != '\n':
        calories = int(calories) + int(i)
    else : 
        elves.append(calories)
        calories = 0

# this is the answer to part 1
mostcal = max(elves)
print(mostcal)

for i in range(3):
    topElves = topElves + mostcal
    elves.remove(mostcal)
    mostcal = max(elves)

#this is the answer to part 2
print(topElves)





