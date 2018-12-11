import string
import random
#random char function
def random_char():
  return random.choice(string.ascii_letters + ' ')

#random 27 char string gen
def random_string(best_dict = {'best_string': ''}, target = ''):
  string = best_dict['best_string']
  new_string = ''
  counter = 0

  if target == '':
    return ''

  if string == '' or len(string) != len(target):
    while counter < len(target):
      string = string + random_char()
      counter = counter + 1
    return string

  while counter < len(target):
    if string[counter] != target[counter]:
      new_string = new_string + random_char()
    else:
      new_string = new_string + string[counter]
    counter = counter + 1
  return new_string

#score random string against target
def score_string(string, target):
  score = 0
  for i in range(len(target)):
    if target[i] == string[i]:
      score = score + 1
    else:
      break
  return score

#keep track of best string
def best_string_comp(string, score, best_dict):
  try:
    best_dict
  except:
    best_dict = {'best_string': '', 'best_score': 0}

  if score > best_dict['best_score']:
    best_dict['best_string'] = string
    best_dict['best_score'] = score
  return best_dict

# check print
def check_print(best_string, best_score):
  check_print.printed = True
  print(best_string, best_score)

#print best guess in 1000
def best_in_a_thousand(index, best_dict):
  check_print.printed = False
  if index%1000 == 0:
    check_print(best_dict['best_string'], best_dict['best_score'])


#repeat string gen and score and print best guess in 1000

def infinite_monkey_theorem(target):
  best_string_and_score = {'best_string': '', 'best_score': 0}
  counter = 0
  while True:
    guess = random_string(best_string_and_score, target)
    score = score_string(guess, target)
    best_string_and_score = best_string_comp(guess, score, best_string_and_score)
    best_in_a_thousand(counter, best_string_and_score)
    if score == len(target):
      break
    counter = counter + 1
  return best_string_and_score



#tests

try:
  best_string_and_score
except:
  best_string_and_score = {'best_string': '', 'best_score': 0}

best_string_and_score = best_string_comp('testString',12, best_string_and_score)

# Generate random char
if isinstance(random_char(), str):
  print('Pass: Generates random char')
else:
  print('Fail: Does not generate random char')

# Generate random 28 char string
if len(random_string(best_string_and_score, 'testString')) == len('testString'):
  print('Pass: Generate random string of equal length to target')
else:
  print('Fail: Does not generate random string of equal length to target')

# Score random string against target
score = score_string(random_string(best_string_and_score,'methinks it is like a weasel'), 'methinks it is like a weasel')
if isinstance(score, int):
  print('Pass: Scores random string against target')
else:
  print('Fail: Does not score random string against target')

# Keep track of best string
try:
  best_string_and_score
except:
  best_string_and_score = {'best_string': '', 'best_score': 0}

best_string_and_score = best_string_comp('testString2',10, best_string_and_score)

if best_string_and_score['best_string'] == 'testString':
  print('Pass: Keeping track of best string')
else:
  print('Fail: Does not keep track of best string')

# Print best guess in 1000
best_in_a_thousand(2,best_string_and_score)
if not check_print.printed:
  print('Pass: Does not print numbers not multiples of 1000')
else:
  print('Fali: Prints numbers that are not multiples of 1000')

best_in_a_thousand(34000, best_string_and_score)

if check_print.printed:
  print('Pass: Prints best guess in 1000')
else:
  print('Fail: Does not print best guess in 1000')

# Run
print(infinite_monkey_theorem('methinks it is like a weasel'))
