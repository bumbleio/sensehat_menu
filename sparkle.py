from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
pixel_list = []


def set_random_rgb():
	rcolor=randint(0,254)
	gcolor=randint(0,254)
	bcolor=randint(0,254)
	return (rcolor, gcolor, bcolor)


for num in range(100000000):
	pixel_list = []		
	for i in range(64):
		color = set_random_rgb()
		pixel_list.append(color)
	# print(pixel_list)
	print(sense.get_temperature())
	sense.set_pixels(pixel_list)
	sleep(1)
	

	



