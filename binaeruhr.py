# Raspberry Pi Pico Pin Overview by StSkanta (TechCree) 838375
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
# Zuordnung der Pins zu den LEDs für die Binaeruhr
#	Feldnr.		GPIO			Binär 	Bezeichnung	Potenz	
#	1	  	GP1				wird nicht benötigt		
#	2	  	GP2				wird nicht benötigt		
#	3	  	GP3				wird nicht benötigt		
#	4	  	GP4				wird nicht benötigt		
#	5	  	GP5				wird nicht benötigt		
#	6 	 	GP6		    8	Stunden	10 'er	
#	7	  	GP7		  	8	Stunden		
#	8	  	GP8		   	8	Minuten	10 'er	
#	9	   GP9		  	8	Minuten		
#	10		GP10				wird nicht benötigt		
#	11		GP11			4	Stunden	10 'er	
#	12		GP12			4	Stunden		
#	13		GP13			4	Minuten	10 'er	
#	14		GP14			4	Minuten		
#	15		GP15				wird nicht benötigt		
#	16		GP16			2	Stunden	10 'er	
#	17		GP17			2	Stunden		
#	18		GP18			2	Minuten	10 'er	
#	19		GP19			2	Minuten		
#	20		GP20				wird nicht benötigt		
#	21		GP21			1	Stunden	10 'er	
#	22		GP22			1	Stunden		
#	23		GP26			1	Minuten	10 'er	
#	24		GP27			1	Minuten		
#	25		GP28				wird nicht benötigt		
#
# Binaeruhr Umsetzung
# Zuordnung der Minuten ###
# 1 "=" 1
# 2 "=" 2
# 3 "=" 1+2
# 4 "=" 4
# 5 "=" 4+1
# 6 "=" 4+2
# 7 "=" 4+2+1
# 8 "=" =8
# 9 "=" 8+1
# 10 "=" 10
#	11	"="	10+1
#	12	"="	10+2
#	13	"="	10+1+2
#	14	"="	10+4
#	15	"="	10+4+1
#	16	"="	10+4+2
#	17	"="	10+4+2+1
#	18	"="	10+8
#	19	"="	10+8+1
#	20	"="	20
#	21	"="	20+1
#	22	"="	20+2
#	23	"="	20+1+2
#	24	"="	20+4
#	25	"="	20+4+1
#	26	"="	20+4+2
#	27	"="	20+4+2+1
#	28	"="	20+8
#	29	"="	20+8+1
#	30	"="	20+8+2
#	31	"="	10+20++1
#	32	"="	10+20++2
#	33	"="	10+20++1+2
#	34	"="	10+20++4
#	35	"="	10+20++4+1
#	36	"="	10+20++4+2
#	37	"="	10+20++4+2+1
#	38	"="	10+20++8
#	39	"="	10+20++8+1
#	40	"="	40
#	41	"="	40+1
#	42	"="	40+2
#	43	"="	40+1+2
#	44	"="	40+4
#	45	"="	40+4+1
#	46	"="	40+4+2
#	47	"="	40+4+2+1
#	48	"="	40+8
#	49	"="	40+8+1
#	50	"="	40+10
#	51	"="	10+40+1
#	52	"="	10+40+2
#	53	"="	10+40+1+2
#	54	"="	10+40+4
#	55	"="	10+40+4+1
#	56	"="	10+40+4+2
#	57	"="	10+40+4+2+1
#	58	"="	10+40+8
#	59	"="	10+40+8+1
#	60	"="	20+40
#
# Zuordnung der Stunden ###
#	1	"="	1
#	2	"="	2
#	3	"="	1+2
#	4	"="	4
#	5	"="	4+1
#	6	"="	4+2
#	7	"="	4+2+1
#	8	"="	8
#	9	"="	8+1
#	10	"="	8+2
#	11	"="	10+1
#	12	"="	10+2
#	13	"="	10+1+2
#	14	"="	10+4
#	15	"="	10+4+1
#	16	"="	10+4+2
#	17	"="	10+4+2+1
#	18	"="	10+8
#	19	"="	10+8+1
#	20	"="	10+8+2
#	21	"="	20+1
#	22	"="	20+2
#	23	"="	20+1+2
#	24	"="	20+4
#
# Start der Uhrzeit und des eigenlichen Skiptes
# Laden der LEDs
import machine
from machine import Pin
import utime

#Led Pins laden nach Feldnr. GPIO sortiert
led25 = Pin(25, Pin.OUT) #mainboard led
#
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
    # Start an LED 25 (mainboard) anzeigen
      led25.value(1)
      utime.sleep(0.1)
      led25.value(0)
      utime.sleep)0.3)
      led25.value(1)
      utime.sleep(0.1)
      led25.value(0)
      
# Starten der Uhr
 ### Minuten Routine 60 Minuten     
### Stunde 0
 ## Minute 1
      utime.sleep(60)
      led24.value(1)	#	1	24	GP27	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led24.value(0)
 ##  Minute 2     
      led19.value(1)	#	2	19	GP19	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led19.value(0)
 ##  Minute 3 
      led24.value(1)	#	3	24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led19.value(0)
      led24.value(0)
 ##   Minute 4  
      led14.value(1)	#	4	14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
 ##   Minute 5    
      led14.value(1)	#	5	14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
      led24.value(0) 
 ##   Minute 6    
      led14.value(1)	#	6	14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
      led19.value(0)
 ##   Minute 7    
      led14.value(1)	#	7	14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0)
      led19.value(0)
      led24.value(0)
 ##   Minute 8    
      led9.value(1)	#	8	9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led9.value(0)
 ##   Minute 9    
      led9.value(1)	#	9	9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led9.value(0)
      led24.value(0)
 ##   Minute 10
      led23.value(1)	#	10	23	GP26	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
 ##   Minute 11    
      led23.value(1)	#	11	23	GP26	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led24.value(0)
 ##   Minute 12
      led23.value(1)	#	12	23	GP26	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led19.value(0)
 ##   Minute 13 
      led23.value(1)	#	13	23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led24.value(0)		
      led19.value(0)		
 ##   Minute 14
      led23.value(1)	#	14	23	GP26	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)
 ##   Minute 15 
      led23.value(1)	#	15	23	GP26	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)	
      led24.value(0)
 ##   Minute 16
      led23.value(1)	#	16	23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)	
      led19.value(0)
 ## Minute 17
      led23.value(1)	#	17	23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 18
      led23.value(1)	#	18	23	GP26	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led9.value(0)
 ## Minute 19
      led23.value(1)	#	19	23	GP26	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led9.value(0)	
      led24.value(0)
 ## Minute 20
      led18.value(1)	#	20	18	GP18	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)
 ## Minute 21
      led16.value(1)	#	21	16	GP16	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led24.value(0)
 ## Minute 22
      led16.value(1)	#	22	16	GP18	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led19.value(0)
 ## Minute 23
      led16.value(1)	#	23	16	GP18	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led19.value(0)	
      led24.value(0)	
 ## Minute 24
      led18.value(1)	#	24	18	GP18	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)
 ## Minute 25
      led18.value(1)	#	25	18	GP18	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)		
      led24.value(0)
 ## Minute 26
      led18.value(1)	#	26	18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)	
      led19.value(0)
 ## Minute 27
      led18.value(1)	#	27	18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 28
      led18.value(1)	#	28	18	GP18	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led9.value(0)
 ## Minute29
      led18.value(1)	#	29	18	GP18	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led9.value(0)		
      led24.value(0)
 ## Minute 30
      led23	.value(1)	#	30	23	GP26	
      led18	.value(1)	#		18	GP18	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23	.value(0)	
      led18	.value(0)
 ## Minute 31
      led23.value(1)	#	31	23	GP26	
      led18.value(1)	#		18	GP18	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led24.value(0)
## Minute 32
      led23.value(1)	#	32	23	GP26	
      led18.value(1)	#		18	GP18	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led19.value(0)
 ## Minute 33
      led23.value(1)	#	33	23	GP26	
      led18.value(1)	#		18	GP18	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
        utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 34
      led23.value(1)	#	34	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led18.value(0)	
      led14.value(0)
 ## Minute 35
      led23.value(1)	#	35	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led14.value(0)		
      led24.value(0)
 ## Minute 36
      led23.value(1)	#	36	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led18.value(0)		
      led14.value(0)		
      led19.value(0)
 ## Minute 37
      led23.value(1)	#	37	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led18.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 38
      led23.value(1)	#	38	23	GP26	
      led18.value(1)	#		18	GP18	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led9.value(0)
 ## Minute 39
      led23.value(1)	#	39	23	GP26	
      led18.value(1)	#		18	GP18	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)
      led9.value(0)	
      led24.value(0)
 ## Minute 40
      led13.value(1)	#	40	13	GP13	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
 ## Minute 41
      led13.value(1)	#	41	13	GP13	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)
 ## Minute 42
      led13.value(1)	#	42	13	GP13	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led19.value(0)
 ## Minute 43
      led13.value(1)	#	43	13	GP13	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 44
      led13.value(1)	#	44	13	GP13	
      led14.value(1)	#		14	GP14
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led14.value(0)
 ## Minute 45
      led13.value(1)	#	45	13	GP13	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led14.value(0)	
      led24.value(0)
 ## Minute 46
      led13.value(1)	#	46	13	GP13	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 47
      led13.value(1)	#	47	13	GP13	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 48
      led13.value(1)	#	48	13	GP13	
      led9.value(1)	#		9	GP9
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten   
      led13.value(0)	#	48	13	GP13	
      led9.value(0)
 ## Minute 49
      led13.value(1)	#	49	13	GP13	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led9.value(0)		
      led24.value(0)
 ## Minute 50
      led13.value(1)	#	50	13	GP13	
      led23.value(1)	#		23	GP26	
     utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)
 ## Minute 51
      led13.value(1)	#	51	13	GP13	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led24.value(0)
 ## Minute 52
      led13.value(1)	#	52	13	GP13	
      led19.value(1)	#		19	GP19	
      led13.value(1)	#		13	GP13
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led19.value(0)	
      led13.value(0)
 ## Minute 53
      led23.value(1)	#	53	23	GP26	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
       utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led23.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 54
      led13.value(1)	#	54	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)		
      led14.value(0)
 ## Minute 55
      led13.value(1)	#	55	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led14.value(0)	
      led24.value(0)
 ## Minute 56
      led13.value(1)	#	56	13	GP13	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
       utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)		
      led24.value(0)		
      led19.value(0)
 ## Minute 57
      led13.value(1)	#	57	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 58
      led13.value(1)	#	58	13	GP13	
      led23.value(1)	#		23	GP26	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led9.value(0)
 ## Minute 59
      led13.value(1)	#	59	13	GP13	
      led23.value(1)	#		23	GP26	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led23.value(0)	
      led9.value(0)	
      led24.value(0)
 ## Minute 60
      led18.value(1)	#	60	18	GP18	
      led13.value(1)	#		13	GP13
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led13.value(0)

### Stunde 1
      led22.value(1)	#	1	22	GP22	
 ## Minute 1
      utime.sleep(60)
      led24.value(1)	#	1	24	GP27	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led24.value(0)
 ##  Minute 2     
      led19.value(1)	#	2	19	GP19	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led19.value(0)
 ##  Minute 3 
      led24.value(1)	#	3	24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led19.value(0)
      led24.value(0)
 ##   Minute 4  
      led14.value(1)	#	4	14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
 ##   Minute 5    
      led14.value(1)	#	5	14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
      led24.value(0) 
 ##   Minute 6    
      led14.value(1)	#	6	14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
      led19.value(0)
 ##   Minute 7    
      led14.value(1)	#	7	14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0)
      led19.value(0)
      led24.value(0)
 ##   Minute 8    
      led9.value(1)	#	8	9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led9.value(0)
 ##   Minute 9    
      led9.value(1)	#	9	9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led9.value(0)
      led24.value(0)
 ##   Minute 10
      led23.value(1)	#	10	23	GP26	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
 ##   Minute 11    
      led23.value(1)	#	11	23	GP26	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led24.value(0)
 ##   Minute 12
      led23.value(1)	#	12	23	GP26	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led19.value(0)
 ##   Minute 13 
      led23.value(1)	#	13	23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led24.value(0)		
      led19.value(0)		
 ##   Minute 14
      led23.value(1)	#	14	23	GP26	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)
 ##   Minute 15 
      led23.value(1)	#	15	23	GP26	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)	
      led24.value(0)
 ##   Minute 16
      led23.value(1)	#	16	23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)	
      led19.value(0)
 ## Minute 17
      led23.value(1)	#	17	23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 18
      led23.value(1)	#	18	23	GP26	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led9.value(0)
 ## Minute 19
      led23.value(1)	#	19	23	GP26	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led9.value(0)	
      led24.value(0)
 ## Minute 20
      led18.value(1)	#	20	18	GP18	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)
 ## Minute 21
      led16.value(1)	#	21	16	GP16	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led24.value(0)
 ## Minute 22
      led16.value(1)	#	22	16	GP18	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led19.value(0)
 ## Minute 23
      led16.value(1)	#	23	16	GP18	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led19.value(0)	
      led24.value(0)	
 ## Minute 24
      led18.value(1)	#	24	18	GP18	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)
 ## Minute 25
      led18.value(1)	#	25	18	GP18	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)		
      led24.value(0)
 ## Minute 26
      led18.value(1)	#	26	18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)	
      led19.value(0)
 ## Minute 27
      led18.value(1)	#	27	18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 28
      led18.value(1)	#	28	18	GP18	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led9.value(0)
 ## Minute29
      led18.value(1)	#	29	18	GP18	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led9.value(0)		
      led24.value(0)
 ## Minute 30
      led23	.value(1)	#	30	23	GP26	
      led18	.value(1)	#		18	GP18	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23	.value(0)	
      led18	.value(0)
 ## Minute 31
      led23.value(1)	#	31	23	GP26	
      led18.value(1)	#		18	GP18	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led24.value(0)
## Minute 32
      led23.value(1)	#	32	23	GP26	
      led18.value(1)	#		18	GP18	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led19.value(0)
 ## Minute 33
      led23.value(1)	#	33	23	GP26	
      led18.value(1)	#		18	GP18	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
        utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 34
      led23.value(1)	#	34	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led18.value(0)	
      led14.value(0)
 ## Minute 35
      led23.value(1)	#	35	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led14.value(0)		
      led24.value(0)
 ## Minute 36
      led23.value(1)	#	36	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led18.value(0)		
      led14.value(0)		
      led19.value(0)
 ## Minute 37
      led23.value(1)	#	37	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led18.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 38
      led23.value(1)	#	38	23	GP26	
      led18.value(1)	#		18	GP18	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led9.value(0)
 ## Minute 39
      led23.value(1)	#	39	23	GP26	
      led18.value(1)	#		18	GP18	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)
      led9.value(0)	
      led24.value(0)
 ## Minute 40
      led13.value(1)	#	40	13	GP13	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
 ## Minute 41
      led13.value(1)	#	41	13	GP13	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)
 ## Minute 42
      led13.value(1)	#	42	13	GP13	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led19.value(0)
 ## Minute 43
      led13.value(1)	#	43	13	GP13	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 44
      led13.value(1)	#	44	13	GP13	
      led14.value(1)	#		14	GP14
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led14.value(0)
 ## Minute 45
      led13.value(1)	#	45	13	GP13	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led14.value(0)	
      led24.value(0)
 ## Minute 46
      led13.value(1)	#	46	13	GP13	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 47
      led13.value(1)	#	47	13	GP13	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 48
      led13.value(1)	#	48	13	GP13	
      led9.value(1)	#		9	GP9
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten   
      led13.value(0)	#	48	13	GP13	
      led9.value(0)
 ## Minute 49
      led13.value(1)	#	49	13	GP13	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led9.value(0)		
      led24.value(0)
 ## Minute 50
      led13.value(1)	#	50	13	GP13	
      led23.value(1)	#		23	GP26	
     utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)
 ## Minute 51
      led13.value(1)	#	51	13	GP13	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led24.value(0)
 ## Minute 52
      led13.value(1)	#	52	13	GP13	
      led19.value(1)	#		19	GP19	
      led13.value(1)	#		13	GP13
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led19.value(0)	
      led13.value(0)
 ## Minute 53
      led23.value(1)	#	53	23	GP26	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
       utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led23.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 54
      led13.value(1)	#	54	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)		
      led14.value(0)
 ## Minute 55
      led13.value(1)	#	55	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led14.value(0)	
      led24.value(0)
 ## Minute 56
      led13.value(1)	#	56	13	GP13	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
       utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)		
      led24.value(0)		
      led19.value(0)
 ## Minute 57
      led13.value(1)	#	57	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 58
      led13.value(1)	#	58	13	GP13	
      led23.value(1)	#		23	GP26	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led9.value(0)
 ## Minute 59
      led13.value(1)	#	59	13	GP13	
      led23.value(1)	#		23	GP26	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led23.value(0)	
      led9.value(0)	
      led24.value(0)
 ## Minute 60
      led18.value(1)	#	60	18	GP18	
      led13.value(1)	#		13	GP13
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led13.value(0)
 ### Stunde 1 Led ausschalten 
      led22.value(0)	
### Stunde 2 
      led17.value(1)	#	2	17	GP17	
## Minute 1
      utime.sleep(60)
      led24.value(1)	#	1	24	GP27	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led24.value(0)
 ##  Minute 2     
      led19.value(1)	#	2	19	GP19	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led19.value(0)
 ##  Minute 3 
      led24.value(1)	#	3	24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led19.value(0)
      led24.value(0)
 ##   Minute 4  
      led14.value(1)	#	4	14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
 ##   Minute 5    
      led14.value(1)	#	5	14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
      led24.value(0) 
 ##   Minute 6    
      led14.value(1)	#	6	14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0) 
      led19.value(0)
 ##   Minute 7    
      led14.value(1)	#	7	14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led14.value(0)
      led19.value(0)
      led24.value(0)
 ##   Minute 8    
      led9.value(1)	#	8	9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led9.value(0)
 ##   Minute 9    
      led9.value(1)	#	9	9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led9.value(0)
      led24.value(0)
 ##   Minute 10
      led23.value(1)	#	10	23	GP26	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
 ##   Minute 11    
      led23.value(1)	#	11	23	GP26	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led24.value(0)
 ##   Minute 12
      led23.value(1)	#	12	23	GP26	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led19.value(0)
 ##   Minute 13 
      led23.value(1)	#	13	23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led24.value(0)		
      led19.value(0)		
 ##   Minute 14
      led23.value(1)	#	14	23	GP26	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)
 ##   Minute 15 
      led23.value(1)	#	15	23	GP26	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)	
      led24.value(0)
 ##   Minute 16
      led23.value(1)	#	16	23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led14.value(0)	
      led19.value(0)
 ## Minute 17
      led23.value(1)	#	17	23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 18
      led23.value(1)	#	18	23	GP26	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led9.value(0)
 ## Minute 19
      led23.value(1)	#	19	23	GP26	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led9.value(0)	
      led24.value(0)
 ## Minute 20
      led18.value(1)	#	20	18	GP18	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)
 ## Minute 21
      led16.value(1)	#	21	16	GP16	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led24.value(0)
 ## Minute 22
      led16.value(1)	#	22	16	GP18	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led19.value(0)
 ## Minute 23
      led16.value(1)	#	23	16	GP18	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led16.value(0)	
      led19.value(0)	
      led24.value(0)	
 ## Minute 24
      led18.value(1)	#	24	18	GP18	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)
 ## Minute 25
      led18.value(1)	#	25	18	GP18	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)		
      led24.value(0)
 ## Minute 26
      led18.value(1)	#	26	18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)	
      led19.value(0)
 ## Minute 27
      led18.value(1)	#	27	18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 28
      led18.value(1)	#	28	18	GP18	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led9.value(0)
 ## Minute29
      led18.value(1)	#	29	18	GP18	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led9.value(0)		
      led24.value(0)
 ## Minute 30
      led23	.value(1)	#	30	23	GP26	
      led18	.value(1)	#		18	GP18	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23	.value(0)	
      led18	.value(0)
 ## Minute 31
      led23.value(1)	#	31	23	GP26	
      led18.value(1)	#		18	GP18	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led24.value(0)
## Minute 32
      led23.value(1)	#	32	23	GP26	
      led18.value(1)	#		18	GP18	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led19.value(0)
 ## Minute 33
      led23.value(1)	#	33	23	GP26	
      led18.value(1)	#		18	GP18	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
        utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 34
      led23.value(1)	#	34	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led18.value(0)	
      led14.value(0)
 ## Minute 35
      led23.value(1)	#	35	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led14.value(0)		
      led24.value(0)
 ## Minute 36
      led23.value(1)	#	36	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)		
      led18.value(0)		
      led14.value(0)		
      led19.value(0)
 ## Minute 37
      led23.value(1)	#	37	23	GP26	
      led18.value(1)	#		18	GP18	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)
      led18.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 38
      led23.value(1)	#	38	23	GP26	
      led18.value(1)	#		18	GP18	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)	
      led9.value(0)
 ## Minute 39
      led23.value(1)	#	39	23	GP26	
      led18.value(1)	#		18	GP18	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led18.value(0)
      led9.value(0)	
      led24.value(0)
 ## Minute 40
      led13.value(1)	#	40	13	GP13	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
 ## Minute 41
      led13.value(1)	#	41	13	GP13	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)
 ## Minute 42
      led13.value(1)	#	42	13	GP13	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led19.value(0)
 ## Minute 43
      led13.value(1)	#	43	13	GP13	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 44
      led13.value(1)	#	44	13	GP13	
      led14.value(1)	#		14	GP14
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led14.value(0)
 ## Minute 45
      led13.value(1)	#	45	13	GP13	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led14.value(0)	
      led24.value(0)
 ## Minute 46
      led13.value(1)	#	46	13	GP13	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 47
      led13.value(1)	#	47	13	GP13	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 48
      led13.value(1)	#	48	13	GP13	
      led9.value(1)	#		9	GP9
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten   
      led13.value(0)	#	48	13	GP13	
      led9.value(0)
 ## Minute 49
      led13.value(1)	#	49	13	GP13	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led9.value(0)		
      led24.value(0)
 ## Minute 50
      led13.value(1)	#	50	13	GP13	
      led23.value(1)	#		23	GP26	
     utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)
 ## Minute 51
      led13.value(1)	#	51	13	GP13	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led24.value(0)
 ## Minute 52
      led13.value(1)	#	52	13	GP13	
      led19.value(1)	#		19	GP19	
      led13.value(1)	#		13	GP13
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led19.value(0)	
      led13.value(0)
 ## Minute 53
      led23.value(1)	#	53	23	GP26	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19	
       utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led23.value(0)	
      led23.value(0)	
      led24.value(0)	
      led19.value(0)
 ## Minute 54
      led13.value(1)	#	54	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)		
      led14.value(0)
 ## Minute 55
      led13.value(1)	#	55	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14	
      led24.value(1)	#		24	GP27
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led14.value(0)	
      led24.value(0)
 ## Minute 56
      led13.value(1)	#	56	13	GP13	
      led23.value(1)	#		23	GP26	
      led24.value(1)	#		24	GP27	
      led19.value(1)	#		19	GP19
       utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)		
      led24.value(0)		
      led19.value(0)
 ## Minute 57
      led13.value(1)	#	57	13	GP13	
      led23.value(1)	#		23	GP26	
      led14.value(1)	#		14	GP14	
      led19.value(1)	#		19	GP19	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led14.value(0)	
      led19.value(0)	
      led24.value(0)
 ## Minute 58
      led13.value(1)	#	58	13	GP13	
      led23.value(1)	#		23	GP26	
      led9.value(1)	#		9	GP9	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)	
      led23.value(0)	
      led9.value(0)
 ## Minute 59
      led13.value(1)	#	59	13	GP13	
      led23.value(1)	#		23	GP26	
      led9.value(1)	#		9	GP9	
      led24.value(1)	#		24	GP27	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led13.value(0)
      led23.value(0)	
      led9.value(0)	
      led24.value(0)
 ## Minute 60
      led18.value(1)	#	60	18	GP18	
      led13.value(1)	#		13	GP13
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led18.value(0)	
      led13.value(0)

  ### Stunde 2 Led ausschalten 
      led17.value(0)	
   
#*****


   ### Stunde 3
       led22.value(1)	#	3	22
       led17.value(1)	#		17
   # Minuten ##
#>
   ### Stunde 3 Led ausschalten 
       led22.value(0)	#	3	22
       led17.value(0)	#		17
   ### Stunde 4
       led12.value(1)	#	4	12
   # Minuten ##
#>
   ### Stunde 4 Led ausschalten 
      led12.value(0)	
   ### Stunde 5
      led12.value(1)	#	5	12
      led22.value(1)	#		22
   # Minuten ##
#>
   ### Stunde 5 Led ausschalten 
      led12.value(0)	#	5	12
      led22.value(0)	#		22
   ### Stunde 6
      led12.value(1)	#	6	12
      led17.value(1)	#		17
   # Minuten ##
#>
  ### Stunde 6 Led ausschalten 
      led12.value(0)	#	6	12
      led17.value(0)	#		17
  ### Stunde 7
      led12.value(1)	#	7	12
      led17.value(1)	#		17
      led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 7 Led ausschalten 
      led12.value(0)	#	7	12
      led17.value(0)	#		17
      led22.value(0)	#		22
   ### Stunde 8
      led7.value(1)	#	8	7
   # Minuten ##
#>
  ### Stunde 8 Led ausschalten 
      led7.value(0)	
  ### Stunde 9 
      led7.value(1)	#	9	7
      led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 9 Led ausschalten 
      led7.value(0)	#	9	7
      led22.value(0)	#		22
  ### Stunde 10 
      led21.value(1)	#	10	21
      led17.value(1)	#		17
   # Minuten ##
#>
  ### Stunde 10 Led ausschalten 
      led21.value(0)	#	10	21
      led17.value(0)	#		17
  ### Stunde 11 
      led21.value(1)	#	11	21
      led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 11 Led ausschalten 
     led21.value(0)	#	11	21
     led22.value(0)	#		22
  ### Stunde 12 
     led21.value(1)	#	12	21
     led17.value(1)	#		17
   # Minuten ##
#>
  ### Stunde 12 Led ausschalten 
     led21.value(0)	#	12	21
     led17.value(0)	#		17
  ### Stunde 13 
     led21.value(1)	#	13	21
     led17.value(1)	#		17
     led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 13 Led ausschalten 
     led21.value(0)	#	13	21
     led17.value(0)	#		17
     led22.value(0)	#		22
  ### Stunde 14 
     led21.value(1)	#	14	21
     led12.value(1)	#		12
   # Minuten ##
#>
  ### Stunde 14 Led ausschalten 
     led21.value(0)	#	14	21
     led12.value(0)	#		12
  ### Stunde 15 
     led21.value(1)	#	15	21
     led12.value(1)	#		12
     led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 15 Led ausschalten 
     led21.value(0)	#	15	21
     led12.value(0)	#		12
     led22.value(0)	#		22
  ### Stunde 16 
     led21.value(1)	#	16	21
     led12.value(1)	#		12
     led17.value(1)	#		17
   # Minuten ##
#>
  ### Stunde 16 Led ausschalten 
     led21.value(0)	#	16	21
     led12.value(0)	#		12
     led17.value(0)	#		17
  ### Stunde 17 
     led21.value(1)	#	17	21
     led12.value(1)	#		12
     led17.value(1)	#		17
     led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 17 Led ausschalten 
     led21.value(0)	#	17	21
     led12.value(0)	#		12
     led17.value(0)	#		17
     led22.value(0)	#		22
  ### Stunde 18 
     led21.value(1)	#	18	21
     led7.value(1)	#		7
   # Minuten ##
#>
  ### Stunde 18 Led ausschalten 
     led21.value(0)	#	18	21
     led7.value(0)	#		7
   ### Stunde 19 
     led21.value(1)	#	19	21
     led7.value(1)	#		7
     led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 19 Led ausschalten 
     led21.value(0)	#	19	21
     led7.value(0)	#		7
     led22.value(0)	#		22
  ### Stunde 20 
     led16.value(1)	#	20	16
   # Minuten ##
#>
  ### Stunde 20 Led ausschalten 
     led16.value(0)	#	20	16
  ### Stunde 21 
     led16.value(1)	#	21	16
     led22.value(1)	#		22
   # Minuten ##
#>
  ### Stunde 21 Led ausschalten 
     led16.value(0)	#	21	16
     led22.value(0)	#		22
  ### Stunde 22 
     led16.value(1)	#	22	16
     led17.value(1)	#		17
   # Minuten ##
#>
  ### Stunde 22 Led ausschalten 
     led16.value(0)	#	22	16
     led17.value(0)	#		17
  ### Stunde 23 
     led16.value(1)	#	23	16
     led17.value(1)	#		17
     led22.value(1)	#		22
  # Minuten ##
#>
  ### Stunde 23 Led ausschalten 
     led16.value(0)	#	23	16
     led17.value(0)	#		17
     led22.value(0)	#		22
   ### Stunde 24 
     led16.value(1)	#	24	16
     led12.value(1)	#		12
  # Minuten ##
#>
  ### Stunde 24 Led ausschalten 
     led16.value(0)	#	24	16
     led12.value(0)	#		12

##### ENDEder Schleife ######################################
