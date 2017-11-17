#
right = []
totalques = 5
q1 = int(input('What is 2 + 99? '))
if q1 == 101:
    print('Yes')
    right.append(q1)
else:
    print('Not')
q2 = int(input('How many letters are in "spell"? '))
if q2 == 5:
    print('Yes')
    right.append(q2)
else:
    print('Not')
q3 = raw_input('What' + "'" + 's that smell? ')
if q3 == "blood" or q3 == "Blood" or q3 == "BLOOD":
    print('Yes')
    right.append(q3)
else:
    print('Not')
q4 = raw_input('How do you spell "this"? ')
if q4 == "this" or q4 == "This" or q4 == "THIS":
    print('Yes')
    right.append(q4)
else:
    print('Not')
while True:
    q5 = raw_input('Which letter: \n A \n B \n C \n ? ')
    if q5 in ["A", "B", "C"]:
        break
if q5 == "A":
    print('Yes')
    right.append(q5)
elif q5 == "B" or q5 == "C":
    print('Not')
if len(right) >= 1:
    percright = (totalques / len(right)) * 100
    print('Final score: ' + str(percright))
else:
    print('Final score: 0')