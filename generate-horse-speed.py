horse1_speed = 1
horse1_stats = eval(open("horses/horse1_stats.txt").read())
track1_stats = eval(open("tracks/track1_stats.txt").read())

## horses ##

for key, value in horse1_stats.iteritems():
	if key == "horse_age":
		horse1_stats_age = value
	if key == "horse_weather":
		horse1_stats_weather = value

## tracks ##

for key, value in track1_stats.iteritems():
	if key == "track_age":
		track1_stats_age = value
	if key == "track_weather":
		track1_stats_weather = value

## speed generator

print track1_stats_age, track1_stats_weather, horse1_stats_age

def generate_horse1_speed(horse1_speed):
	print "function ran"
	if horse1_stats_weather == track1_stats_weather:
		horse1_speed = horse1_speed * 1.2
	else:
		horse1_speed = horse1_speed * 0.8
	if horse1_stats_age <= track1_stats_age:
		horse1_speed = horse1_speed * 1.4
	else:
		horse1_speed = horse1_speed * 0.9
	print horse1_speed
	
generate_horse1_speed(horse1_speed)