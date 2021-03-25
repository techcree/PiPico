#Pico based clock by ssk 838375
s = 0
m = 0
h = 0

import machine
import utime
cls = lambda: print('\n'*100)
#set real time in s for seconds, m for minutes an h for hours clock start then at this time
s = 0
m = 15
h = 9

for count3 in range(24):
  for count2 in range(60):
    for count in range(60):
      cls()  
      s = s + 1
      if s == 60 : s = 0
      print ("Uhrzeit: ",'%02d'%h,":",'%02d'%m,":",'%02d'%s)
      utime.sleep(1)
    s = 0  
    m = m + 1
    if m == 60 : M = 0
  m = 0  
  h = h + 1
 
