import random
from pyfiglet import figlet_format

print(figlet_format('Blackjack!'))

def start_game():
	global cards, player, player_score, comp, comp_score
	suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	values = ['A', '2', '3', '4', '5', '6', '7',
	          '8', '9', '10', 'J', 'Q', 'K']
	cards = [f"{val}_of_{suit}" for val in values for suit in suits]
	random.shuffle(cards)
	player = []
	comp = []
	player_score = 0
	comp_score = 0
	hit(player,2)
	hit(comp,2)
	print(f"\nPlayer's hand: {player}")
	print(f"Dealer's hand: [{comp[0]}, ...?...]")
	player_score = score(player)
	print(f"\nYour score is {player_score}")
	player_move()

def score(hand):
	val = ''
	point = []
	for val in hand:
		if val[0] == 'A':
			point.append(11)
		elif val[0] in ('J', 'Q', 'K'):
			point.append(10)
		else:
			s = val.split("_")
			point.append(int(s[0]))
	total = sum(point)

	if total > 21 and 11 in point:
		for p in range(len(point)):
			if point[p] == 11: point[p] = 1
		total = sum(point)
	elif total > 21:
		print("Bust!")
	return total

def player_move():
	global player_score, player
	choice = ''
	while choice.lower().strip() == '' and player_score <= 21:
		choice = input("Hit or Stand: ")
		if choice.lower().strip() == 'hit':
			choice = ''
			hit(player,1)
			print(f"\nPlayer's hand: {player}")
			player_score = score(player)
			if player_score > 21: final_score()
			print(f"\nPlayer's score is {player_score}")
		elif choice.lower().strip() == 'stand':
			stand()
		else:
			print("Please enter a valid selection")
			choice = ''
	if player_score > 21: final_score()

def hit(user,num):
	global cards
	for i in range(0,num):
		card = cards.pop()
		user.append(card)

def stand():
	global comp, comp_score
	comp_score = 0
	val = ''
	point = []
	for val in comp:
		if val[0] == 'A':
			point.append(11)
		elif val[0] in ('J', 'Q', 'K'):
			point.append(10)
		else:
			s = val.split("_")
			point.append(int(s[0]))
	comp_score = sum(point)

	if comp_score >= 17 and 11 in point:
		for p in range(len(point)):
			if point[p] == 11: point[p] = 1
		comp_score = sum(point)

	if comp_score <= 16: 
		comp_move()
	else:
		print(f"Dealer's hand: {comp}")
		final_score()

def comp_move():
	global comp
	print(f"\nDealer's hand: {comp}")
	print(f"Dealer's score is {comp_score}.")
	print("Dealer takes a card...")
	hit(comp,1)
	# print(f"Dealers hand: {comp}")
	stand()

def final_score():
	global player, player_score, comp, comp_score
	if comp_score == 0: comp_score = score(comp)
	print(f"\nPlayer final score: {player_score}")
	print(f"Dealer final score: {comp_score}\n")
	if player_score <= 21 and (player_score > comp_score or comp_score > 21):
		print("You win!")
	elif (comp_score <= 21 and comp_score > player_score) or player_score > 21:
		print("Better luck next time...")
	elif player_score == comp_score and player_score <= 21:
		print("Tie!")
	new_game = input("\nPlay again (y/n)? ")
	if new_game.lower().strip() in ('n', 'no'):
		print("\nGoodbye!\n")
	elif new_game.lower().strip() in ('y', 'yes'):
		start_game()
	else:
		print("Please enter a valid response.")
		final_score()

start_game()