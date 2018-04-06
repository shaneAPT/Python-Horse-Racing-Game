import os
from generate_race import *
os.system('cls' if os.name == 'nt' else 'clear') ## this clears the cmd so all you see is main menu

current_race = "race"
if active_horses is None:
	active_horses = generate_current_horses()
	horse_speeds = generate_horse_speed() ## speeds are generated this once and stored in a txt afterwards

horse_stats = eval(open("horses/temp_horses.txt").read())
horse_names = eval(open("horses/horse_names.txt").read())
user_money = eval(open("user_money.txt").read())

print " \t\tWelcome to Horse Race!" 
print " ||"+(54 * '=')+"|| \n"
print "\t\t", "Current Balance:", "$"+str(user_money)
print "\tWARNING: Placing a new bet with clear \n\tany previous bet & not return your money"
print " ||"+(54 * '_')+"|| \n"
print "\tACTIVE HORSES:"
print " \t\t"+active_horses[0], "<=>", horse_names[active_horses[0]]
print " \t\t"+active_horses[1], "<=>", horse_names[active_horses[1]]
print " \t\t"+active_horses[2], "<=>", horse_names[active_horses[2]]
print " "+(57 * '=')
print "\n Press:"
print "  ]] 1. Start race   [["
print "  ]] 2. Refresh race [["
print "  ]] 3. Exit game    [[" 

user_input = raw_input(" Enter a menu number:")

if user_input == "1":
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system("python racing_screen.py") ## os.system allows you to run a .py

if user_input == "2":
	os.system("python horserace.py")
