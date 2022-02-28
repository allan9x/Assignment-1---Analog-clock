#source: https://youtu.be/cd4bApAhEIM

#line 35 and 37 were modified to update the hour hand frequently,
# otherwise it will stick to the current hour
#line 64 and 68 were modified to alter
# the hand color to increase contrast to the background image

import time #pulls current time
import tkinter as ui
import math

window = ui.Tk() #instance of window
window.geometry("400x400") #defines size

def update_clock(): #fetches current hours, minutes, and seconds from time module above
    hours = int(time.strftime("%I")) #displays current hour in 12hr system
    minutes = int(time.strftime("%M")) #int converts them into an integer, instead of string
    seconds = int(time.strftime("%S"))

#seconds hand needs to move 360 degrees for 60 seconds. 360/60 = 6 radians/second
#for a detailed explanation of the trigonometic formula below, please visit the timestamped video below
#https://youtu.be/cd4bApAhEIM?t=535

    #updating seconds hand per second
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    #moving 6 radians each second for the seconds hand
    #math.radians is deployed to convert to radians before using it within a Sin function
    #center_x and center_y are used since the hands originate from (200,200), not (0,0)
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)
    #passes updated endpoints of our line, starting with the econds hand, then center of the clock,
    #and finally the calculated values

    #updating minutes hand per minute
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    #6 rad/sec for the seconds hand
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    #updating hours hand per hour + dividing 360 degrees 12 times to determine the hour
    #360/12 = 30, hence (hours * 30...) instead of 6, as used previously
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
    #30 rad/sec for the seconds hand
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock) #updates coordinates every second, passing 1 second to update_clock again

canvas = ui.Canvas(window, width=400, height=400, bg="white") #draws a canvas; sets background as white
canvas.pack(expand=True, fill='both') #fills the canvas with selected color above

#create background
bg = ui.PhotoImage(file='400x.png') #pulls saved image for background of clock
canvas.create_image(200, 200, image=bg) #sets midpoint of image

#create clock hands
center_x = 200 #midpoint as point of origin
center_y = 200 #midpoint as point of origin
seconds_hand_len = 95 #size of hand
minutes_hand_len = 80 #size of hand
hours_hand_len = 60 #size of hand

#drawing clock hands using the line creation method in canvas
#create x and y coordinates of the first endpoint, followed by the second endpoint
seconds_hand = canvas.create_line(200, 200,
                                  200 + seconds_hand_len, 200 + seconds_hand_len,
                                  width=1.5, fill='red')
#minutes hand
minutes_hand = canvas.create_line(200, 200,
                                  200 + minutes_hand_len, 200 + minutes_hand_len,
                                  width = 2, fill = 'gray')
#hours hand
hours_hand = canvas.create_line(200, 200,
                                200 + hours_hand_len, 200 + hours_hand_len,
                                width = 4, fill = 'gray')

update_clock() #updates the clock

window.mainloop()
#tells Python code is between creation of window and the call to the mainloop function