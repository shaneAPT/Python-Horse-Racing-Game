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
print "1. To place bet"
print "2. To start race"
print "3. To Refresh race"
print "4. To view horses"
print "5. To exit" 

user_input = raw_input("Enter a menu number:")

if user_input == "2":
	os.system("python racing_screen.py") ## os.system allows you to run a .py