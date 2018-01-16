import random
##### inputs
# How many samples ?
N = 10**6
# How many doors ?
door = 2

gotcar_nochange = 0
gotcar_change = 0

for i in range(0,N):
	if i % 10**6 == 0:
		print(i)

	car = random.randint(1,door)
	choose = random.randint(1,door)
	reveal = 0
	while (reveal == 0 or reveal == choose or reveal == car):
		reveal = random.randint(1,door) 
	choose2 = 0
	while (choose2 == 0 or choose2 == choose or choose2 == reveal):
		choose2 = random.randint(1,door)

	if choose == car:
		gotcar_nochange += 1
	if choose2 == car:
		gotcar_change += 1

print("Got Car (no change): " , gotcar_nochange,"/",N)
print("% " , gotcar_nochange/N*100)
print("Got Car (change): ", gotcar_change,"/",N)
print("% " , gotcar_change/N*100)