import os
from generate_race import *
os.system('cls' if os.name == 'nt' else 'clear') ## this clears the cmd so all you see is main menu

current_race = "race"
active_horses = generate_current_horses()
horse_odds = generate_odds()
horse_speeds = generate_horse_speed() ## speeds are generated this once and stored in a txt afterwards

print "Welcome to Horse Race!" 
print (20 * '=')
print "Current race:", current_race
print (20 * '=')
print active_horses[0]+",", int(horse_odds[0])
print active_horses[1]+",", int(horse_odds[1])
print active_horses[2]+",", int(horse_odds[2])
print (20 * '=')
print "Press:"
print "1. Place bet"
print "2. Start race"
print "3. Refresh race"
print "4. View horses"
print "5. Exit game" 

user_input = raw_input("Enter a menu number:")

if user_input == "2":
	os.system("python racing_screen.py") ## os.system allows you to run a .py

if user_input == "3":
	os.system("python horserace.py")
