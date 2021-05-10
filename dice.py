import random
from time import sleep

dice_roll1_player = random.randint(1,6)
dice_roll2_player = random.randint(1,6)
print('Your first roll is:', dice_roll1_player, 'and your second roll is:', dice_roll2_player)

sum_dice_player = dice_roll1_player + dice_roll2_player

print("You got dice number of:", sum_dice_player)

dice_roll1_pc = random.randint(1,6)
dice_roll2_pc = random.randint(1,6)

def printd(text, delay=.8):
    print(end=text)
    n_dots = 0

    while True:
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='.', flush=True)
            n_dots += 1
            if n_dots == 3:
            	break
        sleep(delay)

printd('Rolling dice')

sum_dice_pc = dice_roll1_pc + dice_roll2_pc

print("\nComputer's first roll is:", dice_roll1_pc, "and second roll is:", dice_roll2_pc)
print("The computer's dice roll is:", sum_dice_pc)

if sum_dice_player > sum_dice_pc:
	print('Congratulations, you won! :)')
elif sum_dice_player == sum_dice_pc:
	print('We have a draw!! :|')
else:
	print('Sorry, but you lost! :(')

