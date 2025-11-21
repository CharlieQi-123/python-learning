# the sorting hat
# A simple Sorting Hat quiz program, ask 3 questions and score
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')
round1 = int(input('Enter your answer (1-2):'))
if round1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif round1 == 2:
  Hufflepuff += 1
  Slytherin +=1
else:
  print('Wrong input')

print("Q2) When I'm dead, I want people to remember me as:")
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')
round2 = int(input('Enter your answer (1-4):'))
if round2 == 1:
  Hufflepuff += 2
elif round2 == 2:
  Slytherin += 2
elif round2 == 3:
  Ravenclaw += 2
elif round2 == 4:
  Gryffindor += 2
else:
  print('Wrong input')

print("Q3) Which kind of instrument most pleases your ear?")
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')
round3 = int(input('Enter your answer (1-4):'))
if round3 == 1:
  Slytherin += 4
elif round3 == 2:
  Hufflepuff += 4
elif round3 == 3:
  Ravenclaw += 4
elif round3 == 4:
  Gryffindor += 4
else:
  print('Wrong input')

print('The final score:')
print('Gryffindor:',Gryffindor)
print('Ravenclaw:',Ravenclaw)
print('Hufflepuff:',Hufflepuff)
print('Slytherin:',Slytherin)
