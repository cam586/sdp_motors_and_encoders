from motors import Motors
from time import time, sleep

mc = Motors()				# Create an instance of the Motors class used in SDP

motor_id = 3				# The port that your motor is plugged in to
speed = 100 				# forward = positive, backwards = negative
run_time = 2 				# amount of seconds to run motors


mc.move_motor(motor_id,speed)		# Move motor with the given ID at your set speed

start_time = time()

# The encoder board can be a little fragile - always use a try/except loop
try:
	while time() < start_time + run_time:
		mc.print_encoder_data()
		sleep(0.2) 		# Always use a sleep of at least  0.1, or you will get an error
except:
	print "IO Error"

mc.stop_motors()
