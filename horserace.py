import os
os.system('cls' if os.name == 'nt' else 'clear') ## this clears the cmd so all you see is main menu

current_race = "race"

print "Welcome to Horse Race!" 
print (20 * '=')
print "Current race:", current_race
print (20 * '=')
print "horse, horse[odds]"
print "horse, horse[odds]"
print "horse, horse[odds]"
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
