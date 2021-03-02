# Raspberry Pi Pico Pin Overview by StSkanta (TechCree)
# Enter an "X" for your occupied pins
#
#         [X] LED onBoard
# GP0  [ ]  (1)                (40)  [ ] VBUS
# GP1  [x]  (2)                (39)  [ ] VSYS
# GND  [ ]  (3)                (38)  [!] GDN
# GP2  [x]  (4)                (37)  [ ] 3V3_EN
# GP3  [x]  (5)                (36)  [ ] 3V3(OUT)
# GP4  [x]  (6)                (35)  [ ] -
# GP5  [x]  (7)                (34)  [x] GP28
# GND  [ ]  (8)                (33)  [ ] GND
# GP6  [x]  (9)                (32)  [x] GP27
# GP7  [x]  (10)               (31)  [x] GP26
# GP8  [x]  (11)               (30)  [ ] RUN
# GP9  [x]  (12)               (29)  [x] GP22
# GND  [ ]  (13)               (28)  [ ] GND
# GP10 [x]  (14)               (27)  [x] GP21
# GP11 [x]  (15)               (26)  [x] GP20
# GP12 [x]  (16)               (25)  [x] GP19
# GP13 [x]  (17)               (24)  [x] GP18
# GND  [ ]  (18)               (23)  [ ] GDN
# GP14 [x]  (19)               (22)  [x] GP17
# GP15 [x]  (20)               (21)  [x] GP16
#           [ ]SWCLK [ ]GND [ ]SWDIO
#
# Zuordnung LEDs zu einem buchstaben
# A =  2   3   4   6   10  11  12  13  14  15  16  20  21  25
# B =  1   2   3   4   6   10  11  12  13  14  16  20  21  22  23  24
# C =  2   3   4   6   10  11  16  20  22  23  24
# D =  1   2   3   4   6   10  11  15  16  20  21  22  23  24
# E =  1   2   3   4   5   6   11  12  13  14  15  16  21  22  23  24  25
# F =  1   2   3   4   5   6   11  12  13  14  15  16  21
# G =  1   2   3   4   6   10  11  12  13  14  16  21  22  23  24  25
# H =  1   5   6   10  11  12  13  14  15  16  20  21  25
# I =  3   8   13  18  23
# J =  4   9   14  17  19  22  23  24
# K =  1   5   6   9   11  12  13  16  18  21  24
# L =  2   7   12  17  22  23  24
# M =  1   5   6   7   9   10  11  13  15  16  20  21  25
# N =  1   5   6   7   10  11  13  15  16  19  20  21  25
# O =  2   3   4   6   10  11  15  16  20  22  23  24
# P =  1   2   3   4   6   10  11  12  13  16  21
# Q =  2   3   4   6   10  11  13  15  16  19  22  23  25
# R =  1   2   3   4   6   10  11  12  13  14  16  18  21  24
# S =  2   3   4   6   12  13  14  20  22  23  24
# T =  1   2   3   4   5   8   13  18  23
# U =  1   5   6   10  11  15  16  20  22  23  24
# V =  1   5   6   10  11  15  17  19  23
# W =  1   5   6   10  11  13  15  16  17  19  20  21  15
# X =  1   5   7   9   13  17  19  21  25
# Y =  1   5   7   9   13  18  23
# Z =  1   2   3   4   5   9   13  17  21  22  23  24  25
# The LED on the Pico board is the LED PIN 25
# I always let this flash briefly at the start

import machine
from machine import Pin
import utime

#Led Pins laden nach Feldnr. GPIO sortiert
led25 = Pin(25, Pin.OUT) #mainboard led

led1 = Pin(1, Pin.OUT) #GP1
led2 = Pin(2, Pin.OUT) #GP2
led3 = Pin(3, Pin.OUT) #GP3
led4 = Pin(4, Pin.OUT) #GP4
led5 = Pin(5, Pin.OUT) #GP5
led6 = Pin(6, Pin.OUT) #GP6
lde7 = Pin(7, Pin.OUT) #GP7
lde8 = Pin(8, Pin.OUT) #GP8
led9 = Pin(9, Pin.OUT) #GP9
led10 = Pin(10, Pin.OUT) #GP10
led11 = Pin(11, Pin.OUT) #GP11
led12 = Pin(12, Pin.OUT) #GP12
led13 = Pin(13, Pin.OUT) #GP13
led14 = Pin(14, Pin.OUT) #GP14
led15 = Pin(15, Pin.OUT) #GP15
led16 = Pin(16, Pin.OUT) #GP16
led17 = Pin(17, Pin.OUT) #GP17
led18 = Pin(18, Pin.OUT) #GP18
led19 = Pin(19, Pin.OUT) #GP19
led20 = Pin(20, Pin.OUT) #GP20
led21 = Pin(21, Pin.OUT) #GP21
led22 = Pin(22, Pin.OUT) #GP22
led23 = Pin(26, Pin.OUT) #GP26
led24 = Pin(27, Pin.OUT) #GP27
led25 = Pin(28, Pin.OUT) #GP28


while True:
     # Start an LED 25 (mainboard anzeigen)
      led25.value(1)
      utime.sleep(0.1)
      led25.value(0)
      utime.sleep)0.3)
      led25.value(1)
      utime.sleep(0.1)
      led25.value(0)
     ## Ende Startsequenz
      
     # Flash on 
      led1.value(1)
      led2.value(1)
      led3.value(1)
      led4.value(1)
      led5.value(1)
      utime.sleep(0.1)
      led6.value(1)
      led7.value(1)
      led8.value(1)
      led9.value(1)
      led10.value(1)
      utime.sleep(0.1)  
      led11.value(1)
      led12.value(1)
      led13.value(1)
      led14.value(1)
      led15.value(1)
      utime.sleep(0.1)
      led16.value(1)
      led17.value(1)
      led18.value(1)
      led19.value(1)
      led20.value(1)
      utime.sleep(0.1)
      led21.value(1)
      led22.value(1)
      led23.value(1)
      led24.value(1)
      led25.value(1)

     # Pause = Anzeigenzeit in Sekunden (10) = zehn Sekunden
      utime.sleep(0.5)
     ## Ende Flash on

     # Buchstabe anzeigen Beispiel Buchstabe "S"
     # S =  2   3   4   6   12  13  14  20  22  23  24
      led1.value(0)
      led2.value(1)
      led3.value(1)
      led4.value(1)
      led5.value(0)
      utime.sleep(0.1)
      led6.value(1)
      led7.value(0)
      led8.value(0)
      led9.value(0)
      led10.value(0)
      utime.sleep(0.1)
      led11.value(0)
      led12.value(1)
      led13.value(1)
      led14.value(1)
      led15.value(0)
      utime.sleep(0.1)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0)
      led20.value(1)
      utime.sleep(0.1)
      led21.value(0)
      led22.value(1)
      led23.value(1)
      led24.value(1)
      led25.value(0)

      # Pause = Anzeigenzeit in Sekunden (10) = zehn Sekunden
      utime.sleep(10)

      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led1.value(0)
      led2.value(0)
      led3.value(0)
      led4.value(0)
      led5.value(0)
      utime.sleep(0.1)
      led6.value(0)
      led7.value(0)
      led8.value(0)
      led9.value(0)
      led10.value(0)
      utime.sleep(0.1)
      led11.value(0)
      led12.value(0)
      led13.value(0)
      led14.value(0)
      led15.value(0)
      utime.sleep(0.1)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0)
      led20.value(0)
      utime.sleep(0.1)
      led21.value(0)
      led22.value(0)
      led23.value(0)
      led24.value(0)
      led25.value(0)

      # Pause bis zum Neustart = Anzeigenzeit in Sekunden (10) = zehn Sekunden
      utime.sleep(2)

