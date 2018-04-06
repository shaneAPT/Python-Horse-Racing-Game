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
user_money = eval(open("user_money.txt").read())

for key, value in horse_stats.iteritems():
	horse_names.append(key)

for key, value in horse_stats.iteritems():
	horse_speed_list.append(value)

def print_banner():
	print " \t\tWelcome to Horse Race!" 
	print " ||"+(54 * '=')+"|| \n"
	print "\t\t", "Current Balance:", "$"+str(user_money)
	print "\tWARNING: Placing a new bet with clear \n\tany previous bet & not return your money"
	print " ||"+(54 * '_')+"|| \n"
	print "\tACTIVE HORSES:"
	print " \t\t"+horse_names[0], "<=>", horse_names_dict[horse_names[0]]
	print " \t\t"+horse_names[1], "<=>", horse_names_dict[horse_names[1]]
	print " \t\t"+horse_names[2], "<=>", horse_names_dict[horse_names[2]]
	print " ||"+(54 * '=')+"|| \n"
print_banner()

## ----------------- BETTING

current_bet = []

select_horse = input(" Select a horse lane (1, 2, 3):")

while select_horse != 1 and select_horse != 2 and select_horse != 3:
	select_horse = input(" Please select a valid horse (1-3):")

current_bet.append(select_horse)

select_amount = input(" How much would you like to bet?: $")

while int(select_amount) > int(user_money) or select_amount == 0:
	select_amount = input(" Select an amount greater than $0 and within your current balance of $"+str(user_money)+":")

current_bet.append(select_amount)

new_user_money = user_money - select_amount

print " You have placed $"+str(select_amount),"on", horse_names_dict[horse_names[select_horse-1]]+"."
print " Your current balance is now $"+str(new_user_money)+"."

print "\tRace beginning..."
time.sleep(5)

## -------------- HORSES RACING

while leading_horse < race_length:
	horse1_active_pos += horse_speed_list[0]
	horse2_active_pos += horse_speed_list[1]
	horse3_active_pos += horse_speed_list[2]

	print_banner()
	print " "+"="*(int(race_length)+13)+"v"+"====" ## 14 are required to make banner reach end of below strings
	print " |||", " "*int(horse1_active_pos), "("+horse_names[0]+">", " "*(int(race_length)-int(horse1_active_pos)), "|||"
	print " |||", " "*int(horse2_active_pos), "("+horse_names[1]+">", " "*(int(race_length)-int(horse2_active_pos)), "|||"
	print " |||", " "*int(horse3_active_pos), "("+horse_names[2]+">", " "*(int(race_length)-int(horse3_active_pos)), "|||"
	print " "+"="*(int(race_length)+13)+"^"+"====\n"
	print "\tYou currently have: $"+str(select_amount), "on lane", select_horse
	print " ||"+(54 * '=')+"|| \n"
	time.sleep(.15)
	i += 1
	
	if horse1_active_pos > horse2_active_pos and horse1_active_pos > horse3_active_pos:
		leading_horse = horse1_active_pos
		leading_horse_name = horse_names[0]

	elif horse2_active_pos > horse1_active_pos and horse2_active_pos > horse3_active_pos:
		leading_horse = horse2_active_pos
		leading_horse_name = horse_names[1]
	
	else:
		leading_horse = horse3_active_pos
		leading_horse_name = horse_names[2]
	
	if leading_horse < (race_length): ## checks if any horse position is about to exceed the track length
		os.system('cls' if os.name == 'nt' else 'clear')

print "\t\t!!! WINNER:", horse_names_dict[leading_horse_name], "!!!"

if horse_names_dict[leading_horse_name] == horse_names_dict[horse_names[select_horse-1]]: ## if the winning name is the one selected
	new_user_money = user_money+(select_amount*1.5)
	print " YOUR HAVE WON: $"+ str(select_amount*1.5)+"!!\tYOUR BALANCE: $"+str(new_user_money)

else:
	new_user_money = user_money - select_amount

user_money = open("user_money.txt","w")
user_money.write(str(new_user_money))
user_money.close()

print "\tReturning to main menu..."
time.sleep(5)
os.system("python horserace.py") ## returns to main menu after 5 seconds
