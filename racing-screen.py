import os
import time

i = 0
race_length = 60

while i < race_length:
	horse1_speed = (float(i)*.25)
	horse2_speed = (float(i)*1.10)
	horse3_speed = (float(i)*1.04)
	
	print " "*int(horse1_speed), "horse 1", " "*(int(race_length)-int(horse1_speed)), "|||"
	print " "*int(horse2_speed), "horse 2", " "*(int(race_length)-int(horse2_speed)), "||| FINISH"
	print " "*int(horse3_speed), "horse 3", " "*(int(race_length)-int(horse3_speed)), "|||"
	time.sleep(.15)
	os.system('cls' if os.name == 'nt' else 'clear')
	i += 1
	
os.system('cls' if os.name == 'nt' else 'clear')
	