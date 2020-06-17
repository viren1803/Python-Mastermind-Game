import random

print ("  MASTERMIND  \n")
print ("Welkom bij Mastermind! Het is de bedoeling dat je de kleurencode probeert te raden.\n")
print ("Voer je code in!\n Je kan de volgende kleuren gebruiken: rood(R), groen(G), blauw(B), geel(Y), wit(W) en paars(P)")

colors = ["R", "G", "B", "Y", "W", "P"]
attempts = 0
game = True

color_code = random.sample(colors,4)	

while game:
	correct_color = ""
	guessed_color = ""
	player_guess = input().upper()
	attempts += 1
	
	if len(player_guess) != len(color_code):
		print ("\nDe kleurencode heeft maar 4 kleuren, je invoer is te groot!")
		continue
	for i in range(4):
		if player_guess[i] not in colors:
			print ("\nDeze kleur wordt niet in het spel gebruikt. Kijk bovenaan bij de instructies welke kleuren gebruikt worden.")
			continue

if correct_color != "XXXX":
		for i in range(4):
			if player_guess[i] == color_code[i]:
				correct_color += "X"
			if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
				guessed_color += "O"
		print (correct_color +  guessed_color + "\n")		
		
	if correct_color == "XXXX":
		if attempts == 1:
			print ("First try! Lekker bezig!")
		else:
			print ("Goed gedaan, je had " + str(attempts) + " beurten nodig om de code te raden.")
		game = False

if attempts >= 1 and attempts <6 and correct_color != "XXXX":
		print ("Nieuwe ronde, nieuwe kansen: ")
	elif attempts >= 6:
		print ("Het is je niet gelukt! De code was: " + str(color_code))	

while game == False:
		finish_game = input("\nWil je nog een keer spelen? (J/N)?").upper()	
		attempts = 0
		if finish_game =="N":
			print ("Bedankt voor het spelen, doei!")
		elif finish_game == "J":
			game = True
			print ("Zeker weten? Oke dan.. Raad de code: ")