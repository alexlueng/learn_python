import random
import textwrap
import sys


if sys.version_info < (3, 0):
	print("This code requires Python 3.x and is tested with version 3.5.x")
	print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
	print("exiting...")
	exit(1)



if __name__ == '__main__':

	keep_playing = 'y'
	occupants = ['enemy', 'friend', 'unoccupied']

	width = 72
	dotted_line = '-' * width
	print(dotted_line)
	print("\033[1m" + "Attack of The Orcs v0.0.1:" + "\033[1m")
	msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")
	print(textwrap.fill(msg, width=width))
	print("\033[1m" + "Mission:" + "\033[1m")
	print("Choose a hut where Sir Foo can rest...")
	print("\033[1m" + "Be careful as there are enemies lurking around!" + "\033[1m")
	print(dotted_line)

	while keep_playing == 'y':
		huts = []
		for _ in range(5):
			huts.append(random.choice(occupants))

		msg = "\033[1m" + "Choose a hut number to enter(1-5): " + "\033[1m"
		user_choice = input("\n" + msg)
		idx = int(user_choice)

		print("Revealing the occupants...")
		msg = ""
		for i, occ in enumerate(huts):
			occupant_info = "<%d: %s>"%(i+1, occ)
			if i+1 == idx:
				occupant_info = "\033[1m" + "<%d: %s>"%(i+1, occ) + "\033[1m"
			msg += occupant_info

		print("\t" + msg)
		print(dotted_line)
		print("\033[1m" + "Entering hut %d..." % idx + "\033[1m", end=' ')

		if huts[idx-1] == 'enemy':
			print("\033[1m" + "YOU LOSE:( Better luck next time!" + "\033[1m")
		else:
			print("\033[1m" + "YOU WIN!!!!" + "\033[1m")

		keep_playing = input("Play again?Yes(y)No(n)")
