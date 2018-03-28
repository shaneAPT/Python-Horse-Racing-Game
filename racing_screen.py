import os
import time
import random

i = 0
race_length = 40
leading_horse = 0
horse1_active_pos = 0 ## horse active positions are declared here so += is able to work
horse2_active_pos = 0
horse3_active_pos = 0
horse_speed_list = []

horse_stats = eval(open("horses/temp_horses.txt").read())
print horse_stats

for key, value in horse_stats.iteritems():
	horse_speed_list.append(value)


while leading_horse < race_length:
	print horse_speed_list
	horse1_active_pos += horse_speed_list[0]
	horse2_active_pos += horse_speed_list[1]
	horse3_active_pos += horse_speed_list[2]

	print " "+"="*(int(race_length)+14)+"v"+"====" ## 14 are required to make banner reach end of below strings
	print " |||", " "*int(horse1_active_pos), "(horse 1>", " "*(int(race_length)-int(horse1_active_pos)), "|||"
	print " |||", " "*int(horse2_active_pos), "(horse 2>"," "*(int(race_length)-int(horse2_active_pos)), "|||"
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
	
	if leading_horse < (race_length): ## checks if any horse position is about to exceed the track length
		os.system('cls' if os.name == 'nt' else 'clear')

print "!!! WINNER:", leading_horse_name, "!!!"

time.sleep(5)
os.system("python horserace.py") ## returns to main menu after 5 seconds
