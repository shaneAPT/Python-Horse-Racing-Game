import os
from generate_race import *
os.system('cls' if os.name == 'nt' else 'clear') ## this clears the cmd so all you see is main menu

current_race = "race"
active_horses = generate_current_horses()
horse_speeds = generate_horse_speed() ## speeds are generated this once and stored in a txt afterwards

horse_stats = eval(open("horses/temp_horses.txt").read())
horse_names = eval(open("horses/horse_names.txt").read())

print horse_stats

print " \t\tWelcome to Horse Race!" 
print " "+(57 * '=')
print " \t\tCurrent Race:", current_race
print " ="+(55 * '_')+"= "
print " \t\t"+active_horses[0], "<=>", horse_names[active_horses[0]]
print " \t\t"+active_horses[1], "<=>", horse_names[active_horses[1]]
print " \t\t"+active_horses[2], "<=>", horse_names[active_horses[2]]
print " "+(57 * '=')
print "\n Press:"
print "  ]] 1. Place bet    [["
print "  ]] 2. Start race   [["
print "  ]] 3. Refresh race [["
print "  ]] 4. View horses  [["
print "  ]] 5. Exit game    [[" 

user_input = raw_input(" Enter a menu number:")

if user_input == "1":
	os.system("python betting_screen.py")

if user_input == "2":
	os.system("python racing_screen.py") ## os.system allows you to run a .py

if user_input == "3":
	os.system("python horserace.py")
