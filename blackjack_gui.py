import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from random import shuffle
from PIL import Image, ImageTk

# Card images: https://www.flickr.com/photos/167981955@N07/albums/72157716974740172
# Casino image: https://www.freepik.com/free-photo/white-red-blue-casino-chip-stack-green-poker-table_2900667.htm#page=3&query=poker%20table%20background&position=22&from_view=search&track=ais

# define players and function flags
player = []
comp = []
cards = []
player_card_count = len(player)
comp_card_count = len(comp)
shuffled = False
setup = False

def start_game():
	"""setup game: create deck, players, and initial deal"""
	global cards, player, player_score, comp, comp_score, shuffled, player_card_count, comp_card_count
	global player_label_1, player_label_2, player_label_3, player_label_4, player_label_5
	global dealer_label_1, dealer_label_2, dealer_label_3, dealer_label_4, dealer_label_5
	player.clear()
	comp.clear()
	cards.clear()
	player_score = 0
	comp_score = 0
	player_card_count = len(player)
	comp_card_count = len(comp)

	frame_container()
	player_label_1 = tk.Label(player_frame, text='', bg=back_color)
	player_label_1.grid(row=1, column=0, padx=10)
	player_label_2 = tk.Label(player_frame, text='', bg=back_color)
	player_label_2.grid(row=1, column=1, padx=10)
	dealer_label_1 = tk.Label(dealer_frame, image='',  text='', bg=back_color)
	dealer_label_1.grid(row=1, column=0, padx=10)
	dealer_label_2 = tk.Label(dealer_frame, image='',  text='', bg=back_color)
	dealer_label_2.grid(row=1, column=1, padx=10)

	# create and shuffle deck
	suits = ['hearts', 'diamonds', 'clubs', 'spades']
	values = ['A', '2', '3', '4', '5', '6', '7',
	          '8', '9', '10', 'J', 'Q', 'K'
	          ]
	cards = [f"{val}_of_{suit}" for val in values for suit in suits]
	shuffle(cards)
	shuffled = True

	# start dealing cards
	hit(player,2)
	hit(comp,2)
	root.title(f"Blackjack! - {len(cards)} Cards Left")
	
def hit(user=player,num=1):
	"""deal additional card(s) to player or user, default 1 to player"""
	global cards, shuffled, player_card_count, comp_card_count, player_score, comp_score
	global player_frame, player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
	global 				 player_label_1, player_label_2, player_label_3, player_label_4, player_label_5
	global dealer_frame, dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5
	global 				 dealer_label_1, dealer_label_2, dealer_label_3, dealer_label_4, dealer_label_5
	if cards and shuffled:
		# remove card from deck and add to user's hand
		for i in range(0,num):
			card = cards.pop()
			user.append(card)
			root.title(f"Blackjack! - {len(cards)} Cards Left")
			# render image of card in user's hand
			if user == player:
				player_card_count += 1
				if player_card_count == 1:
					player_image_1 = resize_cards(f"images/{card}.jpg")
					player_label_1 = tk.Label(player_frame, image=player_image_1, bg=back_color)
					player_label_1.grid(row=1, column=0, padx=10)
				elif player_card_count == 2:
					player_image_2 = resize_cards(f"images/{card}.jpg")
					player_label_2 = tk.Label(player_frame, image=player_image_2, bg=back_color)
					player_label_2.grid(row=1, column=1, padx=10)
				elif player_card_count == 3:
					player_image_3 = resize_cards(f"images/{card}.jpg")
					player_label_3 = tk.Label(player_frame, image=player_image_3, bg=back_color)
					player_label_3.grid(row=1, column=2, padx=10)
				elif player_card_count == 4:
					player_image_4 = resize_cards(f"images/{card}.jpg")
					player_label_4 = tk.Label(player_frame, image=player_image_4, bg=back_color)
					player_label_4.grid(row=1, column=3, padx=10)
				elif player_card_count == 5:
					player_image_5 = resize_cards(f"images/{card}.jpg")
					player_label_5 = tk.Label(player_frame, image=player_image_5, bg=back_color)
					player_label_5.grid(row=1, column=4, padx=10)
				else:
					messagebox.showinfo("Max Cards", "Maximum cards dealt this hand")
					flip_dealer_card()
					final_score()
			if user == comp:
				comp_card_count += 1
				if comp_card_count == 1:
					dealer_image_1 = resize_cards(f"images/{card}.jpg")
					dealer_label_1 = tk.Label(dealer_frame, image=dealer_image_1, bg=back_color)
					dealer_label_1.grid(row=1, column=0, padx=10)
				elif comp_card_count == 2:
					dealer_image_2 = resize_cards("images/back.jpg")
					dealer_label_2 = tk.Label(dealer_frame, image=dealer_image_2, bg=back_color)
					dealer_label_2.grid(row=1, column=1, padx=10)
				elif comp_card_count == 3:
					dealer_image_3 = resize_cards(f"images/{card}.jpg")
					dealer_label_3 = tk.Label(dealer_frame, image=dealer_image_3, bg=back_color)
					dealer_label_3.grid(row=1, column=2, padx=10)
				elif comp_card_count == 4:
					dealer_image_4 = resize_cards(f"images/{card}.jpg")
					dealer_label_4 = tk.Label(dealer_frame, image=dealer_image_4, bg=back_color)
					dealer_label_4.grid(row=1, column=3, padx=10)
				elif comp_card_count == 5:
					dealer_image_5 = resize_cards(f"images/{card}.jpg")
					dealer_label_5 = tk.Label(dealer_frame, image=dealer_image_5, bg=back_color)
					dealer_label_5.grid(row=1, column=4, padx=10)
				else:
					messagebox.showinfo("Max Cards", "Maximum cards dealt to dealer this hand")
		# calculate player score; comp score/behavior will be managed in stand()
		player_score = score(player)
	# if no cards remain
	elif not cards and shuffled:
		messagebox.showinfo("No Cards", "No cards left")
	# if the cards aren't shuffled yet
	else:
		messagebox.showinfo("No Cards", "Click 'Shuffle' to start the game")

def stand():
	"""end player turn, initiate dealer turn with automatic hit until score > 16"""
	global comp, comp_score, shuffled
	if not shuffled: 
		messagebox.showinfo("No Cards", "Click 'Shuffle' to start the game")
	else:
		comp_score = 0
		val = ''
		point = []
		flip_dealer_card()
		for val in comp:
			if val[0] == 'A':
				point.append(11)
			elif val[0] in ('J', 'Q', 'K'):
				point.append(10)
			else:
				s = val.split("_")
				point.append(int(s[0]))
		comp_score = sum(point)

		if comp_score > 21 and 11 in point:
			for p in range(len(point)):
				if point[p] == 11: point[p] = 1
			comp_score = sum(point)

		if comp_score <= 16: 
			hit(comp)
			stand()
		else:
			final_score()

def score(hand):
	"""score the given hand, account for variable Ace value"""
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
	if hand == player: player_frame.configure(text = f"Player: {total} points")

	if total > 21 and 11 in point:
		for p in range(len(point)):
			if point[p] == 11: point[p] = 1
		total = sum(point)
		if hand == player: player_frame.configure(text = f"Player: {total} points")
	if hand == player and total > 21:
		messagebox.showinfo("Bust", "Bust! Your total exceeds 21!")
		flip_dealer_card()
		new_game()
	return total

def flip_dealer_card():
	"""display dealer's facedown card"""
	global dealer_image_2, dealer_label_2
	dealer_image_2 = resize_cards(f"images/{comp[1]}.jpg")
	dealer_label_2.config(image=dealer_image_2)

def final_score():
	"""recalculate scores for final message: win, lose, tie"""
	comp_score = score(comp)
	player_score = score(player)
	if len(player) >=5 and player_score <= 21:		# Hit after 5th card creates 6th list position before redirecting to final_score()
		messagebox.showinfo("Win", "You were dealt 5 cards without going over 21.\nYou win!")
	elif player_score <= 21 and (player_score > comp_score or comp_score > 21):
		messagebox.showinfo("Win", f"Your score: {player_score}\nDealer score: {comp_score}\nYou win!")
	elif (comp_score <= 21 and comp_score > player_score) or player_score > 21:
		messagebox.showinfo("Lose", f"Your score: {player_score}\nDealer score: {comp_score}\nBetter luck next time...")
	elif player_score == comp_score and player_score <= 21:
		messagebox.showinfo("Tie", f"Your score: {player_score}\nDealer score: {comp_score}\nTie!")
	new_game()

def new_game():
	"""offer new game to player, reset if yes"""
	new_game = messagebox.askquestion("Continue?", "Play again?")
	if new_game == 'no':
		root.destroy()
	else:
		global shuffled
		shuffled = False
		for card in range(0,player_card_count):
			if card==2:
				global player_label_3
				# player_label_3 = tk.Label(player_frame, image='', text='', bg=back_color)
				player_label_3.destroy()
			elif card==3:
				global player_label_4
				player_label_4.destroy()
			elif card==4:
				global player_label_5
				player_label_5.destroy()
		for card in range(0,comp_card_count):
			if card==2:
				global dealer_label_3
				dealer_label_3.destroy()
			elif card==3:
				global dealer_label_4
				dealer_label_4.destroy()
			elif card==4:
				global dealer_label_5
				dealer_label_5.destroy()
		start_game()

def help():
	messagebox.showinfo("Help", "Shuffle: Begin a new game\n"
		"Hit Me: Receive another card\n"
		"Stand!: End your turn, start the dealer's turn\n\n"
		"Blackjack originated in 1960s France, called Vingt-et-Un (French for 21). Its goal is in the name: Score closest to 21 without going over.\n\n"
		"From the shuffle, the dealer and player are dealt 2 cards each, but only one of the dealer's cards is shown. The player may choose to receive one card at a time ('Hit'), ending their turn with 'Stand'. "
		"The dealer flips their hidden card and continues to 'Hit' until their score is higher than 16 or until they 'Bust' (exceed 21). "
		"House rules state that a player who receives (Hits) 5 cards without going over automatically wins.\n\n"
		"Cards are scored as follows:\n"
		"Ace: 1 or 11 points\n"
		"All face cards: 10 points\n"
		"All number cards: Points match the number of the card\n\n"
		"Image Sources:\n"
		"Card: https://www.flickr.com/photos/167981955@N07/albums/72157716974740172\n"
		"Casino: https://www.freepik.com/free-photo/white-red-blue-casino-chip-stack-green-poker-table_2900667.htm#page=3&query=poker%20table%20background&position=22&from_view=search&track=ais")

def resize_cards(card):
	"""make card images from directory smaller"""
	global card_img
	card_img_jpg = Image.open(card)
	card_img_resize = card_img_jpg.resize((130, 188))
	card_img = ImageTk.PhotoImage(card_img_resize)
	return card_img

back_color = "#C6BA9A"	# consistent coloring in frames
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="black")	# color window behind image; ctk radii cut through image and show window
root.title("Blackjack!")

# place background image
bg_image_file = Image.open("images/casino.jpg")
bg_image_resize = bg_image_file.resize((800, 600))
bg_image = ImageTk.PhotoImage(bg_image_resize)
bg = tk.Label(root, image=bg_image)
bg.place(x=0, y=0, relwidth=1, relheight=1)

help_button = ctk.CTkButton(root, 
								text="Help",
								width=20,
								height=30, 
								fg_color="#C6BA9A", 
								text_color="black", 
								corner_radius=5, 
								hover_color="#cccccc", 
								command=help)
help_button.place(x=750, y=13)

# Game buttons
button_frame = ctk.CTkFrame(root, fg_color="black")
button_frame.pack(pady=5)

shuffle_button = ctk.CTkButton(button_frame, text="Shuffle", fg_color=back_color, text_color="black", corner_radius=5, hover_color="#cccccc", command=start_game)
shuffle_button.grid(row=0, column=0, pady=10, padx=5, ipadx=0)

hit_button = ctk.CTkButton(button_frame, text="Hit Me", fg_color=back_color, text_color="black", corner_radius=5, hover_color="#cccccc", command=hit)
hit_button.grid(row=0, column=1, pady=10, padx=5, ipadx=0)

stand_button = ctk.CTkButton(button_frame, text="Stand!", fg_color=back_color, text_color="black", corner_radius=5, hover_color="#cccccc", command=stand)
stand_button.grid(row=0, column=2, pady=10, padx=5, ipadx=0)

# Frames for cards
def frame_container():
	"""upon game start, create card frame GUIs"""
	global setup, player_frame, dealer_frame
	if not setup:
		frame = ctk.CTkFrame(root, fg_color=back_color, corner_radius=5)
		frame.pack(pady=15)

		dealer_frame = ctk.CTkLabel(frame, text="Dealer", text_color="black", corner_radius=10)
		dealer_frame.pack(padx=0, pady=10, ipadx=0, ipady=5)

		player_frame = ctk.CTkLabel(frame, text="Player", text_color="black", corner_radius=10)
		player_frame.pack(padx=0, pady=10, ipadx=0, ipady=5)

		setup = True

root.mainloop()
