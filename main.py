# JOKE GENERATOR V1.2
# MADE BY p0isonedpanda 

import random
import os

# This is our pool of jokes
jokes = ["What did the green grape say to the purple grape?\nBREATHE STUPID!",
		"What happens to a frog's car when it breaks down?\nIt gets toad away.",
		"Why isn't the turkey hungry at Thanks giving?\nBecause it's stuffed.",
		"Why do witches wear name tags?\nSo they know which witch is which.",
		"My friend thinks he is so smart, told me today that onion is the only food that makes you cry\nSo I threw a coconut at his face.",
		"What stays in one corner but travels around the world?\nA stamp.",
		"What do you call a pig that does karate?\nPork chop.",
		"Why does Humpty Dumpty love autumn?\nBecause he had a great fall last year.",
		"Did you hear about the kidnapping at school today?\nIt's alright, he's awake now.",
		"Have you heard about the new restaurant Karma?\nThere's no menu, you get what you deserve."]

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
print "Version 1.2\n"

raw_input("Press [ENTER] for a joke!\n> ")

# Will let us end the program loop if we need to
i = True

# Main program loop where fun stuff happens
while i == True:

	# Simply clears the screen before a new entry appears
	os.system('cls')

	print(jokes[random.randint(0,9)])

	# Checks if we want more jokes or to close
	close = raw_input("Press [ENTER] for another joke or input 'stop' to end\n>")
	if close == 'stop':
		i = False
