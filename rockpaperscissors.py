import random

# images for Rock, Paper, and Scissors
art = [
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
]

# Game messages
results = ["It is a draw", "You win", "You lose"]

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")
choice = int(input("What do you choose? "))

if choice < 0 or choice > 2:
    print("Invalid number. Please choose 0, 1, or 2.")
else:
    comp_random = random.randint(0, 2)

    # Display choices
    print("You chose:")
    print(art[choice])
    print("Computer chose:")
    print(art[comp_random])

    # Determine the result
    if choice == comp_random:
        result = 0  # Draw
    elif (choice - comp_random) % 3 == 1:
        result = 1  # User wins
    else:
        result = 2  # Computer wins

    print(results[result])

def reverse(f1,f2):
  s = Stack()
  fh1 = open(f1, 'r')
  for i in fh1:
    x = i.rstrip('\n')
    s.push(x)
  fh1.close()
 
  fh2 = open(f2, 'w')
  while not s.is_empty():
    y = s.pop()
    fh2.write(y + '\n')
  fh2.close()

