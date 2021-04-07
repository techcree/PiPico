# Raspberry Pi Pico Pin Overview by StSkanta (TechCree) 838375
# Enter an "X" for your occupied pins
#
#                        [X] LED onBoard
#
# led00 GP0  [X]  (1)  sek1                 (40)  [ ] VBUS
# led01 GP1  [X]  (2)  sek2                 (39)  [ ] VSYS
#       GND  [ ]  (3)                       (38)  [X] GDN        LED Panel GDN
# led02 GP2  [X]  (4)  sek4                 (37)  [ ] 3V3_EN
# led03 GP3  [X]  (5)  sek8                 (36)  [X] 3V3(OUT)   RTC Power
# led04 GP4  [X]  (6)  sek10                (35)  [ ] -
# led05 GP5  [X]  (7)  sek20          sek40 (34)  [X] GP28 led06
#       GND  [ ]  (8)                       (33)  [ ] GND
#       GP6  [X]  (9)  (RTCMod)        stu8 (32)  [X] GP27 led19
#       GP7  [X]  (10) (RTCMod)             (31)  [ ] GP26 
# led08 GP8  [X]  (11) min                  (30)  [ ] RUN
# led09 GP9  [X]  (12) min2           stu40 (29)  [X] GP22 led22 
#       GND  [ ]  (13)                      (28)  [ ] GND
# led10 GP10 [X]  (14) min4           stu20 (27)  [X] GP21 led21 
# led11 GP11 [X]  (15) min8             stu (26)  [X] GP20 led20 
# led12 GP12 [X]  (16) min                  (25)  [ ] GP19
# led13 GP13 [X]  (17) min20           stu4 (24)  [X] GP18 led18 
#       GND  [ ]  (18)                      (23)  [ ] GDN
# led14 GP14 [X]  (19) min40           stu2 (22)  [X] GP17 led17 
# led07 GP15 [X]  (20) min80            stu (21)  [X] GP16 led16  
#
#                    [ ]SWCLK [ ]GND [ ]SWDIO
#
# The LED on the Pico board is the LED PIN 25
#
#                Stu                                Min                               Sek
#  80 ()            8 (GP27/led19)    80 ()            8 (GP11/led11)    80 (GP15/led07)  8 (GP3/led03)
#  40 (GP22/led22)  4 (GP18/led18)    40 (GP14/led14)  4 (GP10/led10)    40 (GP28/led06)  4 (GP2/led02)
#  20 (GP21/led21)  2 (GP17/led17)    20 (GP13/led13)  2 (GP9/led09)     20 (GP5/led05)  2 (GP1/led01)
#  10 (GP20/led20)  1 (GP16/led16)    10 (GP12/led12)  1 (GP8/led08)     10 (GP4/led04)  1 (GP0/led00)
#
#
#
# Start Script
import machine
from machine import Pin
import utime


#mainboard LED
led25 =  Pin(25, Pin.OUT)
#
#sekunden Einer
led00 = Pin(0, Pin.OUT) # sek1 gruen (1)
led01 = Pin(1, Pin.OUT) # sek1 gruen (2)
led02 = Pin(2, Pin.OUT) # sek1 gruen (4)
led03 = Pin(3, Pin.OUT) # sek1 gruen (8)
#sekunden Zehner
led04 = Pin(4, Pin.OUT) # sek10 gruen (1) 
led05 = Pin(5, Pin.OUT) # sek10 gruen (2)
#Pin6 wird vom RTC Modul benötigt###
led06 = Pin(28, Pin.OUT) # sek10 gruen (4)
# Pin7 wird vom RTC Modul benötigt###
led07 = Pin(15, Pin.OUT) # sek10 gruen (8)
# Minuten Einer
led08 = Pin(8, Pin.OUT) # min rot (1)
led09 = Pin(9, Pin.OUT) # min rot (2)
led10 = Pin(10, Pin.OUT) # min rot (4)
led11 = Pin(11, Pin.OUT) # min rot (8)
#Minuten Zehner
led12 = Pin(12, Pin.OUT) # min rot (1)
led13 = Pin(13, Pin.OUT) # min rot (2)
led14 = Pin(14, Pin.OUT) # min rot (4)
# min10 (8) rot wird nicht benötigt
#Stunden Einer
led16 = Pin(16, Pin.OUT) # std1 gelb (1)
led17 = Pin(17, Pin.OUT) # std1 gelb (2)
led18 = Pin(18, Pin.OUT) # std1 gelb (4)
led19 = Pin(27, Pin.OUT) # std1 gelb (8)
#Stunden Zehner
led20 = Pin(20, Pin.OUT) # std10 gelb (1)
led21 = Pin(21, Pin.OUT) # std10 gelb (2)
led22 = Pin(22, Pin.OUT) # std10 gelb (4)
# std10 (8) gelb wird nicht benötigt
# Skript zum Testen des LED Panel siehe Zeile 613 Pause muss später nur eine Sekunde sein

while True:
    stu = int(input("Stunden"))
    min =  int(input("Minuten"))
    sek = int(input("Sekunden"))
   
    if sek == 1:
        led00.value(1) 
    if sek == 2:
        led01.value(1)
    if sek == 3:    
        led00.value(1)
        led01.value(1)
    if sek == 4:    
        led02.value(1)
    if sek == 5:    
        led00.value(1)
        led02.value(1)
    if sek == 6:
        led01.value(1)
        led02.value(1)
    if sek == 7:
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 8:    
        led03.value(1)
    if sek == 9:
        led00.value(1)
        led03.value(1)
    if sek == 10:    
        led04.value(1)
    if sek == 11:
        led04.value(1)
        led00.value(1)
    if sek == 12:
        led04.value(1)
        led01.value(1)
    if sek == 13:
        led04.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 14:
        led04.value(1)
        led02.value(1)
    if sek == 15:
        led04.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 16:
        led04.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 17:
        led04.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 18:
        led04.value(1)
        led03.value(1)
    if sek == 19:
        led04.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 20:    
        led05.value(1)
    if sek == 21:
        led05.value(1)
        led00.value(1)
    if sek == 22:
        led05.value(1)
        led01.value(1)
    if sek == 23:
        led05.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 24:
        led05.value(1)
        led02.value(1)
    if sek == 25:
        led05.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 26:
        led05.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 27:
        led05.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 28:
        led05.value(1)
        led03.value(1)
    if sek == 29:
        led05.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 30:    
        led04.value(1)
        led05.value(1)
    if sek == 31:
        led04.value(1)
        led05.value(1)
        led00.value(1)
    if sek == 32:
        led04.value(1)
        led05.value(1)
        led01.value(1)
    if sek == 33:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 34:
        led04.value(1)
        led05.value(1)
        led02.value(1)
    if sek == 35:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 36:
        led04.value(1)
        led05.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 37:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 38:
        led04.value(1)
        led05.value(1)
        led03.value(1)
    if sek == 39:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 40:    
        led06.value(1)
    if sek == 41:
        led06.value(1)
        led00.value(1)
    if sek == 42:
        led06.value(1)
        led01.value(1)
    if sek == 43:
        led06.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 44:
        led06.value(1)
        led02.value(1)
    if sek == 45:
        led06.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 46:
        led06.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 47:
        led06.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 48:
        led06.value(1)
        led03.value(1)
    if sek == 49:
        led06.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 50:
        led04.value(1)
        led06.value(1)
    if sek == 51:
        led04.value(1)
        led06.value(1)
        led00.value(1)
    if sek == 52:
        led04.value(1)
        led06.value(1)
        led01.value(1)
    if sek == 53:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 54:
        led04.value(1)
        led06.value(1)
        led02.value(1)
    if sek == 55:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 56:
        led04.value(1)
        led06.value(1)
        led01.value(1)
        led01.value(1)
    if sek == 57:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 58:
        led04.value(1)
        led06.value(1)
        led03.value(1)
    if sek == 59:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led03.value(1)
    if sek >= 60:
        print("falsche Eingabe")
    if min == 1:    
        led08.value(1)
    if min == 2:        
        led09.value(1)
    if min == 3:
        led08.value(1)
        led09.value(1)
    if min == 4:    
        led10.value(1)
    if min == 5:
        led08.value(1)
        led10.value(1)      
    if min == 6:
        led09.value(1)
        led10.value(1)
    if min == 7:
        led08.value(1)
        led09.value(1)
        led10.value(1)  
    if min == 8:
        led11.value(1)
    if min == 9:
        led08.value(1)
        led11.value(1)
    if min >= 10:
        print("falsche Eingabe")        
    if min == 10:
        led12.value(1)
    if min == 11:
        led12.value(1)
        led08.value(1)
    if min == 12:
        led12.value(1)
        led09.value(1)
    if min == 13:
        led12.value(1)
        led08.value(1)
        led09.value(1)
    if min == 14:
        led12.value(1)
        led10.value(1)
    if min == 15:
        led12.value(1)
        led08.value(1)
        led10.value(1)
    if min == 16:
        led12.value(1)
        led09.value(1)
        led10.value(1)
    if min == 17:
        led12.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)
    if min == 18:
        led12.value(1)
        led11.value(1)
    if min == 19:
        led12.value(1)
        led08.value(1)
        led11.value(1)
    if min == 20:
        led13.value(1)
    if min == 21:
        led13.value(1)
        led08.value(1)
    if min == 22:
        led13.value(1)        
        led09.value(1)
    if min == 23:
        led13.value(1)
        led08.value(1)
        led09.value(1)
    if min == 24:
        led13.value(1)    
        led10.value(1)
    if min == 25:
        led13.value(1)
        led08.value(1)
        led10.value(1)      
    if min == 26:
        led13.value(1)
        led09.value(1)
        led10.value(1)
    if min == 27:
        led13.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)  
    if min == 28:
        led13.value(1)
        led11.value(1)
    if min == 29:
        led13.value(1)
        led08.value(1)
        led11.value(1)
    if min == 30:
        led12.value(1)
        led13.value(1)
    if min == 31:
        led12.value(1)
        led13.value(1)
        led08.value(1)
    if min == 32:
        led12.value(1)
        led13.value(1)        
        led09.value(1)
    if min == 33:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led09.value(1)
    if min == 34:
        led12.value(1)
        led13.value(1)    
        led10.value(1)
    if min == 35:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led10.value(1)      
    if min == 36:
        led12.value(1)
        led13.value(1)
        led09.value(1)
        led10.value(1)
    if min == 37:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)  
    if min == 38:
        led12.value(1)
        led13.value(1)
        led11.value(1)
    if min == 39:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led11.value(1)
    if min == 40:
        led14.value(1)
    if min == 41:
        led14.value(1)
        led08.value(1)
    if min == 42:
        led14.value(1)
        led09.value(1)
    if min == 43:
        led14.value(1)
        led08.value(1)
        led09.value(1)
    if min == 44:
        led14.value(1)
        led10.value(1)
    if min == 45:
        led14.value(1)
        led08.value(1)
        led10.value(1)
    if min == 46:
        led14.value(1)
        led09.value(1)
        led10.value(1)
    if min == 47:
        led14.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)
    if min == 48:
        led14.value(1)
        led11.value(1)
    if min == 49:
        led14.value(1)
        led08.value(1)
        led11.value(1)
    if min == 50:
        led12.value(1)
        led14.value(1)
    if min == 51:
        led12.value(1)
        led14.value(1)
        led08.value(1)
    if min == 52:
        led12.value(1)
        led14.value(1)
        led09.value(1)
    if min == 53:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led09.value(1)
    if min == 54:
        led12.value(1)
        led14.value(1)
        led10.value(1)
    if min == 55:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led10.value(1)
    if min == 56:
        led12.value(1)
        led14.value(1)
        led09.value(1)
        led10.value(1)
    if min == 57:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)
    if min == 58:
        led12.value(1)
        led14.value(1)
        led11.value(1)
    if min == 59:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led11.value(1)
    if min >= 60:
         print("falsche Eingabe")
    if stu == 1:        
        led16.value(1)
    if stu == 2:
        led17.value(1)
    if stu == 3:
        led16.value(1)
        led17.value(1)
    if stu == 4:
        led18.value(1)
    if stu == 5:
        led16.value(1)
        led18.value(1)
    if stu == 6:
        led17.value(1)
        led18.value(1)
    if stu == 7:
        led16.value(1)
        led17.value(1)
        led18.value(1)
    if stu == 8:
        led19.value(1)
    if stu == 9:
        led16.value(1)
        led19.value(1)
    if stu >= 10:   
        print("falsche Eingabe")
    if stu == 10:        
        led20.value(1)
    if stu == 11:
        led20.value(1)
        led16.value(1)
    if stu == 12:
        led20.value(1)
        led17.value(1)
    if stu == 13:
        led20.value(1)
        led16.value(1)
        led17.value(1)
    if stu == 14:
        led20.value(1)
        led18.value(1)
    if stu == 15:
        led20.value(1)
        led16.value(1)
        led18.value(1)
    if stu == 16:
        led20.value(1)
        led17.value(1)
        led18.value(1)
    if stu == 17:
        led20.value(1)
        led16.value(1)
        led17.value(1)
        led18.value(1)
    if stu == 18:
        led20.value(1)
        led19.value(1)
    if stu == 19:
        led20.value(1)
        led16.value(1)
        led19.value(1)
    if stu == 20:        
        led21.value(1)
    if stu == 21:
        led21.value(1)
        led16.value(1)
    if stu == 22:
        led21.value(1)
        led17.value(1)
    if stu == 23:
        led21.value(1)
        led16.value(1)
        led17.value(1)
    if stu == 24: #??
        led21.value(1)
        led18.value(1)
    if stu >= 30:
        print("falsche Eingabe")
#nicht verwendete LED
#        led22.value(1)
#        led24.value(1)
    else:
        utime.sleep(10)
#        print("Fertig")
        #Reset
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
