
X = 1
Z = 3
# number of points
points = int(0)

f = open('inputday2.txt', 'r')
lines = f.readlines()

for i in lines:
    if i[2] == "Y":
        points += 2
    elif i[2] == "X":
        points += 1
    else:
        points += 3
     
for i in lines:
    if i[0] == "A":
        #opponent choose rock
        if i[2] == "Y":
            points += 6
        elif i[2] == "X":
            points += 3
    elif i[0] == "B":
        #opponent choose paper
        if i[2] == "Y":
            points += 3
        elif i[2] == "Z":
            points += 6
    if i[0] == "C":
        #opponent choose scissor
        if i[2] == "X":
            points += 6
        elif i[2] == "Z":
            points += 3
# answer to part 1
print(points)
#reset ponts for part 2
points = 0
draw = 3
win = 6
rock = 1
paper = 2
scissor = 3
# part 2 
# X = loose, Y = draw, Z = win

def uavgjort(motstander):
        poeng = 0
        if motstander == "A":
            poeng += 1
        elif motstander == "B":
            poeng += 2
        elif motstander == "C":
            poeng += 3
        return poeng

def vinn(motstander):
    poeng = 0
    if motstander == "A":
        poeng += paper
    elif motstander == "B":
        poeng += scissor
    elif motstander == "C":
        poeng += rock
    return poeng

def tap(motstander):
    poeng = 0
    if motstander == "A":
        poeng += scissor
    elif motstander == "B":
        poeng += rock
    elif motstander == "C":
        poeng += paper
    return poeng


for i in lines:
    # you need to loose
    if i[2] == "X":
        points += tap(i[0])
    #you need to draw
    elif i[2] == "Y":
        points += draw + uavgjort(i[0])
    #you need to win
    elif i[2] == "Z":
        points += win + vinn(i[0])

print(points)


