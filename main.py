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