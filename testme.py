import RPi.GPIO as GPIO
from time import sleep
import pygame
from random import randint

#Variables
#Sounds
snake = "wrong.mp3"
ladder = "correct.mp3"


#Resistors
r13 = 14
r39 = 15
r67 = 18
r72 = 23
#Pythons
s38 = 24
s47 = 25
s68 = 8
s99 = 7

#LED

d1 = 12
d2 = 16
d3 = 20
d4 = 21
d5 = 5
d6 = 6

#Button
button = 13

#Configuration

pygame.init()
pygame.mixer.init()

GPIO.setmode(GPIO.BCM)
for pin in [r13, r39, r67, r72, s38, s47, s68, s99, button]:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

leds = [d1, d2, d3, d4, d5, d6]
for led in leds:
	GPIO.setup(led, GPIO.OUT)

GPIO.output(d2,0)

#Function to play sounds
def play_sound(x):
	pygame.mixer.music.load(x)
	pygame.mixer.music.play(1)
	while pygame.mixer.get_busy() == True:
		continue


#Function to roll dice
def dice():
	roll = randint(1,6)
	print(roll)
	
	# turn on the number of LEDs specified by roll
	for led in leds[:roll]:
		GPIO.output(led, 1)
	
	sleep(3)
	
	# turn them off
	for led in leds[:roll]:
		GPIO.output(led, 0)


while True:
    if GPIO.input(r13) == True:
        print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(r39) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(r67) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(r72) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(s38) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(s47) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(s68) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(s99) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(button) == True:
    	dice()
    	sleep(1)