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
horse_names = []

horse_stats = eval(open("horses/temp_horses.txt").read())
horse_names_dict = eval(open("horses/horse_names.txt").read())
for key, value in horse_stats.iteritems():
	horse_names.append(key)

print horse_stats

for key, value in horse_stats.iteritems():
	horse_speed_list.append(value)


while leading_horse < race_length:
	print horse_speed_list
	horse1_active_pos += horse_speed_list[0]
	horse2_active_pos += horse_speed_list[1]
	horse3_active_pos += horse_speed_list[2]

	print " "+"="*(int(race_length)+13)+"v"+"====" ## 14 are required to make banner reach end of below strings
	print " |||", " "*int(horse1_active_pos), "("+horse_names[0]+">", " "*(int(race_length)-int(horse1_active_pos)), "|||"
	print " |||", " "*int(horse2_active_pos), "("+horse_names[1]+">", " "*(int(race_length)-int(horse2_active_pos)), "|||"
	print " |||", " "*int(horse3_active_pos), "("+horse_names[2]+">", " "*(int(race_length)-int(horse3_active_pos)), "|||"
	print " "+"="*(int(race_length)+13)+"^"+"===="
	print " ||=-=\t\t", horse_names[0], "=", horse_names_dict[horse_names[0]]
	print " ||=-=\t\t", horse_names[1], "=", horse_names_dict[horse_names[1]]
	print " ||=-=\t\t", horse_names[2], "=", horse_names_dict[horse_names[2]]
	print " "+"="*(int(race_length)+18)
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

print "\t\t!!! WINNER:", leading_horse_name, "!!!"

time.sleep(5)
os.system("python horserace.py") ## returns to main menu after 5 seconds
