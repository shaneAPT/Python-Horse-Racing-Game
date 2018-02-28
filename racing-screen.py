import os
import time
import random

i = 0
race_length = 30
leading_horse = 0

while leading_horse < race_length:
	horse1_speed = (float(i)*.25)
	horse2_speed = (float(i)*1.40)
	horse3_speed = (float(i)*1.04)
	
	print " "+"="*(int(race_length)+14)+"v"+"====" ## 14 are required to make banner reach end of below strings
	print " |||", " "*int(horse1_speed), "(horse 1>", " "*(int(race_length)-int(horse1_speed)), "|||"
	print " |||", " "*int(horse2_speed), "(horse 2>"," "*(int(race_length)-int(horse2_speed)), "||| FINISH"
	print " |||", " "*int(horse3_speed), "(horse 3>", " "*(int(race_length)-int(horse3_speed)), "|||"
	print " "+"="*(int(race_length)+14)+"^"+"===="
	## print leading_horse ## purely for debug
	time.sleep(.15)
	i += 1
	
	if horse1_speed > horse2_speed and horse1_speed > horse3_speed:
		leading_horse = horse1_speed
		leading_horse_name = "Horse 1"

	elif horse2_speed > horse1_speed and horse2_speed > horse3_speed:
		leading_horse = horse2_speed
		leading_horse_name = "Horse 2"
	
	else:
		leading_horse = horse3_speed
		leading_horse_name = "Horse 3"
	
	if leading_horse < (race_length):
		os.system('cls' if os.name == 'nt' else 'clear') ## if nobody has won the track refreshes and positions update

print "!!! WINNER:", leading_horse_name, "!!!"