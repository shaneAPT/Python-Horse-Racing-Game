import random
import math

active_horses = []
horses = ["horse1", "horse2", "horse3", "horse4", "horse5"]
tracks = ["track1", "track2", "track3"]
current_track_stats = eval(open("tracks/"+tracks[random.randint(0,len(tracks)-1)]+"_stats.txt").read())

def generate_current_horses():
	while len(active_horses) < 3:
		temp_active_horse = "horse"+str(random.randint(1,5))
		if temp_active_horse not in active_horses: ## needed so the same horse is not running twice in one race
			active_horses.append(temp_active_horse)
	return active_horses
generate_current_horses()

def generate_odds():
	speed_dict = eval(open("horses/temp_horses.txt").read())
	temp_speed_sum = 0
	horse_odds = []
	for line in active_horses:
		temp_speed_sum += speed_dict[str(line)]
	for line in active_horses:
		horse_odds.append(math.ceil((speed_dict[line] / temp_speed_sum) * 100 + 100))
	return horse_odds

for key, value in current_track_stats.iteritems():
	if key == "track_age":
		track1_stats_age = value
	if key == "track_weather":
		track1_stats_weather = value

def generate_horse_speed():
	horse_generated_speeds = {}
	j = 0
	while j < len(active_horses):
		file_path = "horses/"+active_horses[j]+"_stats.txt"
		temp_horse = eval(open(file_path).read()) ## reading the dictionary from the stats file in /horses/
		for key, value in temp_horse.iteritems(): ## assigning each value in the dictionary to a variable
			if key == "horse_age":
				temp_horse_age = value
			if key == "horse_weather":
				temp_horse_weather = value
			if key == "jockey_age":
				jockey_age = value
			if key == "horse_consistency":
				horse_consistency = value
			if key == "horse_jumping":
				horse_jumping = value

		temp_horse_speed = 1
		if temp_horse_weather == track1_stats_weather: ## if the horse and weather track preference (0 or 1) match
			temp_horse_speed = temp_horse_speed * 1.2
		else:
			temp_horse_speed = temp_horse_speed * 1.09
		if temp_horse_age <= track1_stats_age: ## if the horse is younger than the track is it favoured.
			temp_horse_speed = temp_horse_speed * 1.46
		else:
			temp_horse_speed = temp_horse_speed + .2
		if jockey_age <= track1_stats_age:
			temp_horse_speed = temp_horse_speed * 0.82
		else:
			temp_horse_speed = temp_horse_speed * 1.28
		if horse_consistency == 1:
			temp_horse_speed = temp_horse_speed + .10
		if horse_jumping == 1:
			temp_horse_speed = temp_horse_speed + .5
		else:
			temp_horse_speed = temp_horse_speed *.2

		horse_generated_speeds[active_horses[j]] = temp_horse_speed
		j += 1

	######## writes the horse speeds to a txt file
	f = open("horses/temp_horses.txt","w")
	f.write(str(horse_generated_speeds))
	f.close()
	######## 
	return horse_generated_speeds

generate_horse_speed()
