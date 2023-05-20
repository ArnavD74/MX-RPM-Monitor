import RPi.GPIO as GPIO
import csv
import time
from datetime import datetime
import os

GPIO.setmode(GPIO.BOARD)

# Define two button pins
button_pins = [7, 13]
for button_pin in button_pins:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define separate counts and start times for each button
button_counts = [0, 0]
start_times = [time.time(), time.time()]

def reset_count(button_index):
    global button_counts, start_times
    button_counts[button_index] = 0
    start_times[button_index] = time.time()

def button_callback(channel):
    button_index = button_pins.index(channel)
    button_counts[button_index] += 1
    print("Button {} Pressed! Count: {}".format(button_index, button_counts[button_index]))
    with open('count{}.csv'.format(button_index), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "actuations", "actuations/min", "actuations/hr"])
        elapsed_time = time.time() - start_times[button_index]
        writer.writerow([datetime.now(), button_counts[button_index], button_counts[button_index]/(elapsed_time/60), button_counts[button_index]/(elapsed_time/3600)])

for button_pin in button_pins:
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=130)

try:
    while True:
        for button_index, button_pin in enumerate(button_pins):
            if os.path.exists('reset{}.txt'.format(button_index)):
                reset_count(button_index)
                os.remove('reset{}.txt'.format(button_index))
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

