import time
from PIL import ImageGrab
import pydirectinput
import keyboard
from random import random

mode = 0
x=0
randomThrow = 0

#infinite while loop to keep the program running in the background
while (x != 100):
    px = ImageGrab.grab().load() #screen shot of your screen is taken, must be in window mode in Knockout City

    if keyboard.is_pressed('l'): #press l to quit the program
        quit()
    
    #4 pixels are taken as a sample to determine if the ball is thrown at you
    color = px[1, 1]
    color2= px[1, 10]
    color3= px[1, 100]
    color4= px[1, 50]

    if keyboard.is_pressed('r'):  # if key 'r' is pressed 
        print('Run mode activated!')
        mode = 1 #mode 1 is activated, aka run away mode, dashes everytime a ball is thrown at you
    
    elif keyboard.is_pressed('c'):  # if key 'c' is pressed 
        print('Catch mode activated!')
        mode = 0 #mode 0 is activated, aka catch everytime a ball is thrown at you    

    elif keyboard.is_pressed('t'):  # if key 'c' is pressed 
        print('Throw mode activated!')
        mode = 3 #mode 3 is activated, aka catch and throw everytime a ball is thrown at you         
        

    #checks if a ball has been thrown at you
    if ((color == (255, 255, 255) or color2 == (255, 255, 255) or color3 == (255, 255, 255) or color4 == (255, 255, 255))): 

            #player will catch using the key 'p' (Bind catch to p)
        if mode == 0:
            pydirectinput.keyDown('p')
            time.sleep(0.05)
            pydirectinput.keyUp('p')

            #player will dash using the key 'o' (Bind dash to p)
        elif mode == 1: 
            pydirectinput.keyDown('o')
            time.sleep(0.05)
            pydirectinput.keyUp('o')

            #player will catch and look to throw using the key 'p' and then the left click to throw(Bind catch to p)
        elif mode == 3: 
            pydirectinput.keyDown('p')
            time.sleep(0.05)
            pydirectinput.keyUp('p')

            #throw is randomly either 1 fake or an insta throw based off of the radnom number generated
            randomThrow = random() % 10

            if (randomThrow < 5):
                pydirectinput.click()
                pydirectinput.mouseUp()

            elif (randomThrow < 9):
                time.sleep(0.1)
                pydirectinput.keyDown('f')
                time.sleep(0.05)
                pydirectinput.keyUp('f')
                time.sleep(0.1)
                pydirectinput.keyDown('f')
                time.sleep(0.05)
                pydirectinput.keyUp('f')
                pydirectinput.click()
                pydirectinput.mouseUp()

            elif (randomThrow >= 9):
                pydirectinput.click()
                pydirectinput.mouseUp()
        


            

            
          
            