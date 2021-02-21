# clear Display

import machine 
import utime 

# Pico Display boilerplate
import picodisplay as display
width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)

# Set the display backlight to 50%
display.set_backlight(0.5)

i = 0


def clear():  
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()

while True: 
        clear()      
