from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()

olive = [93, 159, 65]
pink = [255, 0, 255]
blue = [0, 0, 255]
purple = [157, 64, 229]
black = [0, 0, 0]
red = [255, 0, 0]
grey = [192, 192, 192]
brown = [102, 51, 0]
colors = [ olive, pink, blue ]


def get_user_input():
	return input("Please Select Option: ")

def get_color(what_to_color):
	return input("Select " + what_to_color + " Color: ")

def set_backgroup_color(color):
	sense.clear(color)
	
def show_a_letter(letter):
	sense.show_letter(letter, text_colour=[ 99, 99, 200 ], back_colour=[255,0,0])
	
def choose_random_color():
	random_red = randint(0, 255)
	random_green = randint(0, 255)
	random_blue = randint(0, 255)
	return (random_red, random_green, random_blue)
	
def choose_random_int():
	random_int = randint(0, 7)
	return random_int

def set_pixel_color(pixel_x, pixel_y, color):
	sense.set_pixel(pixel_x, pixel_y, color)
	

def write_message(message, bg_color, txt_color):
	sense.show_message(message, back_colour=bg_color, text_colour=txt_color)

def print_temp():
	print(sense.get_temperature())



while True:
	print("SenseHat Play Menu")
	print(" ")
	print("1 - Set Backgroud Color ")
	print("2 - Write Message ")
	print("3 - Write A letter ")
	print("4 - make random colours")
	print("5 - illuminate random pixel with random color")
	print("6 - print temperature")
	print("X - Exit program ")
	option = get_user_input()
	if option == "1":
		# eval converts a string to a predined variable name
		gb_color = eval(get_color("backgroup"))
		set_backgroup_color(gb_color)
	elif option == "2":
		gb_color = eval(get_color("backgroup"))
		txt_color = eval(get_color("text"))
		write_message(input("Write a message to sense hat: "), gb_color , txt_color)
	elif option == "3":
		show_a_letter(input("display a letter"))
	elif option == "4":
		for i in range(100):
			random_color=choose_random_color()
			set_backgroup_color(random_color)
			sleep(1)
	elif option == "5":
		for i in range(100):
			random_color=choose_random_color()
			random_x = choose_random_int()
			random_y = choose_random_int()
			set_pixel_color(random_x, random_y, random_color)
			sleep(1)
	elif option == "6":
		print_temp()
	elif option == "X":
		sense.clear()
		break
		
		
		
	




