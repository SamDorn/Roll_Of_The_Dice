import random
dice_1 = []
dice_2 = []
random_1 = 0
random_2 = 0
tot_1 = 0
tot_2 = 0
draw = 0
print("Inserisci i valori del primo dado")
for i in range(6):
	dice_1.append( int(input("")))
print("Inserisci il valore del secondo dado")
for i in range(6):
	dice_2.append(int(input("")))

for i in range(1001):
	random_1 = random.choice(dice_1)
	random_2 = random.choice(dice_2)
	if(random_1 > random_2):
		tot_1 += 1
	elif(random_1 < random_2):
		tot_2 +=1
	else:
		draw +=1
if(tot_1 > tot_2):
	print(f"Il vincitore è il primo dado con {tot_1} vittorie, {tot_2} sconfitte e {draw} pareggi")
elif(tot_1 < tot_2):
	print(f"Il vincitore è il secondo dado con {tot_2} vittorie, {tot_1} sconfitte e {draw} pareggi")
else:
	print(f"Pareggio")

	