# created, copyed and modified by 838375 V4.0
# Temperaturmessung und Anzeige mit Display und Buttons

import machine 
import utime
from machine import ADC #mainboardsensor
from machine import Pin
import picodisplay as display # Pico Display boilerplate
import time, random

width = display.get_width()
height = display.get_height()

display_buffer = bytearray(width * height * 2)
display.init(display_buffer)
display.set_backlight(0.5)

#picodisplay.set_led(255, 0, 0)

sensor_temp = machine.ADC(4) # reads from Pico's temp sensor 
conversion_factor = 3.3 / (65535) #converts it into a more manageable number
display.set_backlight(0.5) # Set the display backlight to 50%

led25 = Pin(25, Pin.OUT) #mainboard LED
#led06 = Pin(6, Pin.OUT) #Pimoroni Board LED  rot
#led07 = Pin(7, Pin.OUT) #Pimoroni Board LED  gruen
#led08 = Pin(8, Pin.OUT) #Pimoroni Board LED  blau

def clear():  
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()

def resetLeds():
    led06.value(0)
    led07.value(0)
    led08.value(0)
    led25.value(0)
    resetLeds()
    
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q
        
h = 0
o = 0
clear()

while True:
    if display.is_pressed(display.BUTTON_A):              
        clear()
        display.set_pen(0, 0, 139)
        display.rectangle(0, 0, 300, 140)
        display.set_pen(255, 255, 255)
        display.text("Hello", 10, 10, 240, 3)
        display.text("World", 10, 40, 240, 3)
        display.text("Python", 10, 70, 240, 3)
        display.text("is great", 10, 100, 240, 3)
        display.update()
        utime.sleep(5)
        clear()
    
    elif display.is_pressed(display.BUTTON_B):
        clear()
        display.set_pen(0, 0, 139)
        display.rectangle(0, 0, 300, 140)
        display.set_pen(255, 255, 255)
        display.text("by ssk 838375", 10, 10, 240, 4)
        display.update()
        utime.sleep(5)
        clear()
    elif display.is_pressed(display.BUTTON_X):
        clear()
               
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = round(27 - (reading - 0.706) / 0.001721)    
        display.set_pen(0, 0, 139)
        display.rectangle(0, 0, 300, 140)
        display.set_pen(255, 255, 255)
        display.text("Temperatur:", 10, 30, 0, 3)
        display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 7) 
        display.update()
        utime.sleep(10) 
        display.clear()
        clear()
        
    elif display.is_pressed(display.BUTTON_Y):
        clear()
        t_end = time.time() + 60 * 1
        while time.time() < t_end:
            h += 1
            r, g, b = [int(255 * c) for c in hsv_to_rgb(h / 360.0, 1.0, 1.0)]  
            display.set_led(r, g, b)  
            display.set_pen(r, g, b)
            o = +1
            display.clear()           
            display.set_pen(0, 0, 0)  
            display.text("GAMING", 80, 60, 240, 3)
            display.update()
            utime.sleep(0.01)
            display.clear()
   
    else:
        display.set_pen(255, 255, 255)
        display.text("X=Temp", 148, 15, 240, 3)
        display.set_pen(0, 255, 0)
        display.text("A=Well", 10, 15, 240, 3)
        display.set_pen(255, 0, 0)
        display.text("Pi Pico", 80, 60, 240, 3)
        display.set_pen(255, 0, 255)
        display.text("B=Sign", 10, 100, 240, 3)
        display.set_pen(0, 255, 255)
        display.text("Y=RGB", 148, 100, 240, 3)
        display.update()
utime.sleep(0.1)  
