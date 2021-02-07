# Lets blink LEDs conected with your Raspberry Pi Pico by SKANTA (TechCree) 
# Enter an "X" for your occupied pins
#
#         [X] LED onBoard
# GP0  [ ]  (1)                (40)  [ ] VBUS
# GP1  [ ]  (2)                (39)  [ ] VSYS
# GND  [ ]  (3)                (38)  [ ] GDN
# GP2  [ ]  (4)                (37)  [ ] 3V3_EN
# GP3  [ ]  (5)                (36)  [ ] 3V3(OUT)
# GP4  [ ]  (6)                (35)  [ ] -
# GP5  [ ]  (7)                (34)  [ ] GP28
# GND  [ ]  (8)                (33)  [ ] GND
# GP6  [ ]  (9)                (32)  [ ] GP27
# GP7  [ ]  (10)               (31)  [ ] GP26
# GP8  [ ]  (11)               (30)  [ ] RUN
# GP9  [ ]  (12)               (29)  [ ] GP22
# GND  [ ]  (13)               (28)  [ ] GND
# GP10 [X]  (14)               (27)  [ ] GP21 
# GP11 [X]  (15)               (26)  [ ] GP20
# GP12 [X]  (16)               (25)  [ ] GP19
# GP13 [X]  (17)               (24)  [X] GP18
# GND  [ ]  (18)               (23)  [ ] GDN
# GP14 [X]  (19)               (22)  [X] GP17
# GP15 [X]  (20)               (21)  [X] GP16
#           [ ]SWCLK [ ]GND [ ]SWDIO
#
import machine
from machine import Pin
import utime

led25 =  Pin(25, Pin.OUT) #mainboard 

led18 =  Pin(18, Pin.OUT) #rot
led17 =  Pin(17, Pin.OUT) #gruen
led16 =  Pin(16, Pin.OUT) #blau
led15 =  Pin(15, Pin.OUT) #rot
led14 =  Pin(14, Pin.OUT) #gruen
led13 =  Pin(13, Pin.OUT) #blau
led12 =  Pin(12, Pin.OUT) #rot
led11 =  Pin(11, Pin.OUT) #gruen
led10 =  Pin(10, Pin.OUT) #blau


while True:
#Start wird signalisiert
     led25.value(1)
     utime.sleep(0.1)
     led25.value(0)
     utime.sleep(0.1)
     led25.value(1)
     utime.sleep(0.1)
     led25.value(0)
# Start abgeschlossen
# start rot
     led15.value(1)
     utime.sleep(0.5)
     led12.value(1)
     utime.sleep(0.5)
     led18.value(1)
     utime.sleep(15) #Pause
     led15.value(0)
     utime.sleep(0.5)
     led12.value(0)
     utime.sleep(0.5)
     led18.value(0)
# start gruen     
     led14.value(1)
     utime.sleep(0.2)
     led11.value(1)
     utime.sleep(0.2)
     led17.value(1)
     utime.sleep(15) #Pause
     led14.value(0)
     utime.sleep(0.5)
     led11.value(0)
     utime.sleep(0.5)
     led17.value(0)
# start blau     
     led13.value(1)
     utime.sleep(0.2)
     led10.value(1)
     utime.sleep(0.2)
     led16.value(1)
     utime.sleep(15) #Pause
     led13.value(0)
     utime.sleep(0.5)
     led10.value(0)
     utime.sleep(0.5)
     led16.value(0)
# start mix
     led14.value(1)
     led10.value(1)
     led15.value(1)
     led16.value(1)
     led17.value(1)
     led18.value(1)
     utime.sleep(15) #Pause
     led14.value(0)
     led10.value(0)
     led15.value(0)
     led16.value(0)
     led17.value(0)
     led18.value(0)

     utime.sleep(0.1)
