horse_stats_dict = eval(open("horses/temp_horses.txt").read())
horse_names = eval(open("horses/horse_names.txt").read())
user_money = eval(open("user_money.txt").read())

print user_money

active_horses = []

for key, value in horse_stats_dict.iteritems():
	active_horses.append(key)

print " ||"+(54 * '=')+"|| \n"
print "\t\t", "Current Balance:", "$"+str(user_money)
print " ||"+(54 * '_')+"|| \n"
print " \t\t"+"Horse 1", "<=>", horse_names[active_horses[0]]
print " \t\t"+"Horse 2", "<=>", horse_names[active_horses[1]]
print " \t\t"+"Horse 3", "<=>", horse_names[active_horses[2]]
print " ||"+(54 * '_')+"|| \n"

current_bet = []

select_horse = raw_input(" Select a horse (Example: '1'):")

while select_horse != "1" and select_horse != "2" and select_horse != "3":
	select_horse = raw_input(" Please select a valid horse (1-3):")

current_bet.append(select_horse)

select_amount = raw_input(" How much would you like to bet?:")

while int(select_amount) <= 0 and select_amount > user_money:
	select_amount = raw_input(" Select an amount greater than $0 and within your current balance:")

current_bet.append(select_amount)

print current_bet




##f = open("horses/temp_horses.txt","w")
##print f
##f.write(str(horse_generated_speeds))
##f.close()