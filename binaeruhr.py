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
#	6 		GP6		    8	Stunden	10 'er	
#	7	  	GP7		  	8	Stunden		
#	8	   	GP8		   	8	Minuten	10 'er	
#	9	    GP9		  	8	Minuten		
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
# Minuten ###
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
#	20	"="	10+8+2
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
#	40	"="	10+20++8+2
#	41	"="	40+1
#	42	"="	40+2
#	43	"="	40+1+2
#	44	"="	40+4
#	45	"="	40+4+1
#	46	"="	40+4+2
#	47	"="	40+4+2+1
#	48	"="	40+8
#	49	"="	40+8+1
#	50	"="	40+8+2
#	51	"="	10+40+1
#	52	"="	10+40+2
#	53	"="	10+40+1+2
#	54	"="	10+40+4
#	55	"="	10+40+4+1
#	56	"="	10+40+4+2
#	57	"="	10+40+4+2+1
#	58	"="	10+40+8
#	59	"="	10+40+8+1
#	60	"="	10+40+8+2
#
# Stunden ###
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
## Minute 1
      utime.sleep(60)
      led24.value(1)	#	1	24	GP27	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led1.value(0)
      led2.value(0)
      led3.value(0)
      led4.value(0)
      led5.value(0)
      led6.value(0)
      led7.value(0)
      led8.value(0)
      led9.value(0)
      led10.value(0)
      led11.value(0)
      led12.value(0)
      led13.value(0)
      led14.value(0)
      led15.value(0)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0)
      led20.value(0)
      led21.value(0)
      led22.value(0)
      led23.value(0)
      led24.value(0)
      led25.value(0)
##  Minute 2     
      led19.value(1)	#	2	19	GP19	
      utime.sleep(60)
     # jetzt alle LED/Pins zurücksetzen/ausschalten
      led1.value(0)
      led2.value(0)
      led3.value(0)
      led4.value(0)
      led5.value(0)
      led6.value(0)
      led7.value(0)
      led8.value(0)
      led9.value(0)
      led10.value(0)
      led11.value(0)
      led12.value(0)
      led13.value(0)
      led14.value(0)
      led15.value(0)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0)
      led20.value(0)
      led21.value(0)
      led22.value(0)
      led23.value(0)
      led24.value(0)
      led25.value(0)
##  Minute 3 
      led24.value(1)	#	3	24	GP27	
      led19.value(1)	#		19	GP19	
      utime.sleep(60)
      # jetzt alle LED/Pins zurücksetzen/ausschalten
      led1.value(0)
      led2.value(0)
      led3.value(0)
      led4.value(0)
      led5.value(0)
      led6.value(0)
      led7.value(0)
      led8.value(0)
      led9.value(0)
      led10.value(0)
      led11.value(0)
      led12.value(0)
      led13.value(0)
      led14.value(0)
      led15.value(0)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0)
      led20.value(0)
      led21.value(0)
      led22.value(0)
      led23.value(0)
      led24.value(0)
      led25.value(0)
##   Minute 4  
    led14.value(1)	#	4	14	GP14	
##   Minute 5    
    led14.value(1)	#	5	14	GP14	
    led24.value(1)	#		24	GP27	
##   Minute 6    
    led14.value(1)	#	6	14	GP14	
    led19.value(1)	#		19	GP19	
##   Minute 7    
    led14.value(1)	#	7	14	GP14	
    led19.value(1)	#		19	GP19	
    led24.value(1)	#		24	GP27	
##   Minute 8    
    led9.value(1)	#	8	9	GP9	
##   Minute 9    
    led9.value(1)	#	9	9	GP9	
    led24.value(1)	#		24	GP27	
##   Minute 10
    led23.value(1)	#	10	23	GP26	
##   Minute 11    
led	23	.value(1)	#	11	23	GP26	
led	24	.value(1)	#		24	GP27	
##   Minute 12
led	23	.value(1)	#	12	23	GP26	
led	19	.value(1)	#		19	GP19	
##   Minute 13 
led	23	.value(1)	#	13	23	GP26	
led	24	.value(1)	#		24	GP27	
led	19	.value(1)	#		19	GP19	
##   Minute 14
led	23	.value(1)	#	14	23	GP26	
led	14	.value(1)	#		14	GP14	
##   Minute 15 
led	23	.value(1)	#	15	23	GP26	
led	14	.value(1)	#		14	GP14	
led	24	.value(1)	#		24	GP27	
##   Minute 16
led	23	.value(1)	#	16	23	GP26	
led	14	.value(1)	#		14	GP14	
led	19	.value(1)	#		19	GP19	

##### und so weiter...
