import random
import time
cards = []
for a in range (100):
	cards.append(random.sample(range(1,80),5))
print (cards)
sumar = 0
my_Bingo_Numbers = []
t = float(input('Give the time between each number draw '))
t_2 = float(input('Give the time between each next draw of numbers start'))
for atempts in range (1000):
	count = 0
	counter = 0
	cond = True
	while True:
		for i in range (80):
			while True:
				f = 0
				my_Bingo_Numbers.append(random.randrange(1,80,1))
				for x in range (len(my_Bingo_Numbers)- 1):
					if my_Bingo_Numbers[i] == my_Bingo_Numbers[x]:
						f = f + 1
				if f > 0:
					del my_Bingo_Numbers[i]
				else:
					break
			if cond == False:
				break
			print (my_Bingo_Numbers)
			count = count + 1
			if i > 4:
				for b in range (len(cards)):
					counter = 0
					for c in range (5):
						if cards[b][c] in my_Bingo_Numbers:
							counter = counter + 1
							if counter == 5:
								print ('Bingo for player ', b)
								cond = False			
			time.sleep(t)	
		break
	my_Bingo_Numbers.clear()
	sumar = sumar + count
	time.sleep(t_2)
M_O = sumar/1000
print ('It needs an Aevrage of ', M_O,'or rounded up', round(M_O), 'draws of number to have bingo!')





