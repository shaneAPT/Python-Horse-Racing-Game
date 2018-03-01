track1_stats = eval(open("tracks/track1_stats.txt").read())
horses = ["horse1", "horse2", "horse3"]

## tracks ##

for key, value in track1_stats.iteritems():
	if key == "track_age":
		track1_stats_age = value
	if key == "track_weather":
		track1_stats_weather = value

def generate_horse_speed():
	horse_generated_speeds = {}
	j = 0
	while j < len(horses):
		file_path = "horses/"+horses[j]+"_stats.txt"
		temp_horse = eval(open(file_path).read()) ## reading the dictionary from the stats file in /horses/
		for key, value in temp_horse.iteritems(): ## assigning each value in the dictionary to a variable
			if key == "horse_age":
				temp_horse_age = value
			if key == "horse_weather":
				temp_horse_weather = value

		temp_horse_speed = 1
		if temp_horse_weather == track1_stats_weather: ## if the horse and weather track preference (0 or 1) match
			temp_horse_speed = temp_horse_speed * 1.2
		else:
			temp_horse_speed = temp_horse_speed * 0.8
		if temp_horse_age <= track1_stats_age: ## if the horse is younger than the track is it favoured.
			temp_horse_speed = temp_horse_speed * 1.4
		else:
			temp_horse_speed = temp_horse_speed * 0.9
		horse_generated_speeds[horses[j]] = temp_horse_speed
		j += 1
	return horse_generated_speeds
