import os
import time
import random

i = 0
race_length = 30
leading_horse = 0
horse1_active_pos = 0 ## horse active positions are declared here so += is able to work
horse2_active_pos = 0
horse3_active_pos = 0
horse1_speed = 1 # these speeds will be drawn from a dictionairy of the horses stats
horse2_speed = 2
horse3_speed = 3


while leading_horse < race_length:
	horse1_active_pos += horse1_speed
	horse2_active_pos += horse2_speed
	horse3_active_pos += horse3_speed
	
	print " "+"="*(int(race_length)+14)+"v"+"====" ## 14 are required to make banner reach end of below strings
	print " |||", " "*int(horse1_active_pos), "(horse 1>", " "*(int(race_length)-int(horse1_active_pos)), "|||"
	print " |||", " "*int(horse2_active_pos), "(horse 2>"," "*(int(race_length)-int(horse2_active_pos)), "||| FINISH"
	print " |||", " "*int(horse3_active_pos), "(horse 3>", " "*(int(race_length)-int(horse3_active_pos)), "|||"
	print " "+"="*(int(race_length)+14)+"^"+"===="
	## print leading_horse ## purely for debug
	time.sleep(.15)
	i += 1
	
	if horse1_active_pos > horse2_active_pos and horse1_active_pos > horse3_active_pos:
		leading_horse = horse1_active_pos
		leading_horse_name = "Horse 1"

	elif horse2_active_pos > horse1_active_pos and horse2_active_pos > horse3_active_pos:
		leading_horse = horse2_active_pos
		leading_horse_name = "Horse 2"
	
	else:
		leading_horse = horse3_active_pos
		leading_horse_name = "Horse 3"
	
	if leading_horse < (race_length):
		os.system('cls' if os.name == 'nt' else 'clear') ## if nobody has won the track refreshes and positions update

print "!!! WINNER:", leading_horse_name, "!!!"