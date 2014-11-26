# JOKE GENERATOR V1.0
# MADE BY p0isonedpanda 

# Here we import the random module
import random

# This is our pool of jokes
j1 = "What did the green grape say to the purple grape?\nBREATHE STUPID!"
j2 = "What happens to a frog's car when it breaks down?\nIt gets toad away."
j3 = "Why isn't the turkey hungry at Thanks giving?\nBecause it's stuffed."
j4 = "Why do witches wear name tags?\nSo they know which witch is which."
j5 = "My friend thinks he is so smart, told me today that onion is the only food that makes you cry\nSo I threw a coconut at his face."
j6 = "What stays in one corner but travels around the world?\nA stamp."
j7 = "What do you call a pig that does karate?\nPork chop."
j8 = "Why does Humpty Dumpty love autumn?\nBecause he had a great fall last year."
j9 = "Did you hear about the kidnapping at school today>\nIt's alright, he's awake now."
j10 = "Have you heard about the new restaurant Karma?\nThere's no menu, you get what you deserve."

# Placeholder for raw_input parameter
para = "Press [ENTER] for a joke!\n> "
para2 = "Press [ENTER] for another joke or input 'stop' to end\n>"

# Start up screen
print "Welcome to the"
print "       _       _        "
print "      | |     | |       "
print "      | | ___ | | _____ "
print "  _   | |/ _ \| |/ / _ \\"
print " | |__| | (_) |   <  __/"
print "  \____/ \___/|_|\_\___|"
print "   _____                           _             "
print "  / ____|                         | |            "
print " | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ "
print " | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|"
print " | |__| |  __/ | | |  __/ | | (_| | || (_) | |   "
print "  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   "
print "Presented by p0isonedpanda"
print "Version 1.0\n"

raw_input(para)

# Will let us end the program loop if we need to
i = True

# Main program loop where fun stuff happens
while i == True:

	# Simply clears the screen before a new entry appears
	print '\n' * 100

	joke = random.randint(1, 10)

	if joke == 1:
		print j1
	elif joke == 2:
		print j2
	elif joke == 3:
		print j3
	elif joke == 4:
		print j4
	elif joke == 5:
		print j5
	elif joke == 6:
		print j6
	elif joke == 7:
		print j7
	elif joke == 8:
		print j8
	elif joke == 9:
		print j9
	elif joke == 10:
		print j10

	# Checks if we want more jokes or to close
	close = raw_input(para2)
	if close == 'stop':
		i = False
