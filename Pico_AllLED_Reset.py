# Raspberry Pi Pico Pin Overview by StSkanta (TechCree) 838375
#LED Reset 

import machine
from machine import Pin
import utime

led00 = Pin(0, Pin.OUT) # sek1 gruen (1)
#mainboard LED
led25 =  Pin(25, Pin.OUT)
#
led00 = Pin(0, Pin.OUT) # sek1 gruen (1)
led01 = Pin(1, Pin.OUT) # sek1 gruen (2)
led02 = Pin(2, Pin.OUT) # sek1 gruen (4)
led03 = Pin(3, Pin.OUT) # sek1 gruen (8)
led04 = Pin(4, Pin.OUT) # sek10 gruen (1) 
led05 = Pin(5, Pin.OUT) # sek10 gruen (2)
led06 = Pin(28, Pin.OUT) # sek10 gruen (4)
led07 = Pin(15, Pin.OUT) # sek10 gruen (8)
led08 = Pin(8, Pin.OUT) # min rot (1)
led09 = Pin(9, Pin.OUT) # min rot (2)
led10 = Pin(10, Pin.OUT) # min rot (4)
led11 = Pin(11, Pin.OUT) # min rot (8)
led12 = Pin(12, Pin.OUT) # min rot (1)
led13 = Pin(13, Pin.OUT) # min rot (2)
led14 = Pin(14, Pin.OUT) # min rot (4)
led16 = Pin(16, Pin.OUT) # std1 gelb (1)
led17 = Pin(17, Pin.OUT) # std1 gelb (2)
led18 = Pin(18, Pin.OUT) # std1 gelb (4)
led19 = Pin(27, Pin.OUT) # std1 gelb (8)
led20 = Pin(20, Pin.OUT) # std10 gelb (1)
led21 = Pin(21, Pin.OUT) # std10 gelb (2)
led22 = Pin(22, Pin.OUT) # std10 gelb (4)

while True:
    #Reset LEDS
     led00.value(0) 
     led01.value(0) 
     led02.value(0) 
     led03.value(0) 
     led04.value(0) 
     led05.value(0) 
     led06.value(0) 
     led07.value(0)
     led08.value(0) 
     led09.value(0)
     led10.value(0)
     led11.value(0)
     led12.value(0)
     led13.value(0)
     led14.value(0)
#        led15.value(0)
     led16.value(0)
     led17.value(0)
     led18.value(0)
     led19.value(0)
     led20.value(0)
     led21.value(0)
     led22.value(0)
#        led24.value(0)
