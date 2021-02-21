# Kopie von Pimoroni angepasst durch stskanta ###2
# Temperaturanzeige mit wechselndem Farbschema für Pico onboard temp.-sensor

import machine 
import utime 

# Pico Display
import picodisplay as display
width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)

# Lesen vom Pico's temp.-sensor und konvertieren in lesbares Zahlenformat
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535) 

# Einstellung für Display Hintergrundbeleuchtung in % (0,5 = 50%)
display.set_backlight(0.7)
i = 0

# Start
while True:
# Erste Auswahl mit Taste A
  if display.is_pressed(display.BUTTON_A): 
    # Umrechnung der Nummernform des Pico senors in Grad Celsius
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721)    
   
    # Farbe für den Hintergrund des Textes festlegen bspw. (0, 0, 139) = dunkelblau
    display.set_pen(0, 0, 139)
    display.rectangle(0, 0, 300, 140)
    
    # Unterlegen des Textes in andere Farbe und Text und Textfarbe festlegen
    display.set_pen(255, 255, 255)
    display.text("Temperatur:", 10, 30, 0, 3)
    display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 5) 
    
    # Update Display
    display.update()
    
    # Pause in Sekunden
    utime.sleep(5)
    
# Zweite Auswahl mit Taste B in anderer Farbe
  elif display.is_pressed(display.BUTTON_B):   
    # Umrechnung der Nummernform des Pico senors in Grad Celsius
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721)    

    # Hintergrund
    display.set_pen(255, 255, 255)
    display.rectangle(0, 0, 300, 140)
    
    # Text, Texthintergrund und Textfarbe festlegen
    display.set_pen(0, 0, 0)
    display.text("Temperatur:", 10, 30, 0, 3)
    display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 5) 
    
    # Update Display
    display.update()
    
    # Pause in Sekunden
    utime.sleep(5)

# Dritte Auswahl mit Taste X in anderer Farbe
  elif display.is_pressed(display.BUTTON_X):   
    # Umrechnung der Nummernform des Pico senors in Grad Celsius
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721)    

    # Hintergrund
    display.set_pen(153, 50, 204)
    display.rectangle(0, 0, 300, 140)
    
    # Text, Texthintergrund und Textfarbe festlegen
    display.set_pen(255, 255, 255)
    display.text("Temperatur:", 10, 30, 0, 3)
    display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 5) 
    
    # Update Display
    display.update()
    
    # Pause in Sekunden
    utime.sleep(5)
    

# Dritte Auswahl mit Taste Y in anderer Farbe
  elif display.is_pressed(display.BUTTON_Y):   
    # Umrechnung der Nummernform des Pico senors in Grad Celsius
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721)    

    # Hintergrund
    display.set_pen(0, 255, 0)
    display.rectangle(0, 0, 300, 140)
    
    # Text, Texthintergrund und Textfarbe festlegen
    display.set_pen(0, 0, 0)
    display.text("Temperatur:", 10, 30, 0, 3)
    display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 5) 
    
    # Update Display
    display.update()
    
    # Pause in Sekunden
    utime.sleep(5)
    
  else:      
#    # Umrechnung der Nummernform des Pico senors in Grad Celsius
#    reading = sensor_temp.read_u16() * conversion_factor
#    temperature = round(27 - (reading - 0.706) / 0.001721)    

#    # Farbe für den Hintergrund des Textes festlegen bspw. (0, 0, 139) = dunkelblau
#    display.set_pen(0, 0, 0)
#   display.rectangle(0, 0, 0, 0)
    
#    # Unterlegen des Textes in andere Farbe und Text und Textfarbe festlegen
#    display.set_pen(0, 0, 0)
#    display.text("Temperatur:", 10, 30, 0, 3)
#    display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 5) 

   else:
        display.set_pen(255, 255, 0)                    
        display.text("Hallo Stephan!", 10, 10, 240, 4)
        display.update()
    utime.sleep(0.1)  # this number is how frequently the Pico checks for button presses
#    # Update Display
#    display.update()

#    # Pause in Sekunden
#    utime.sleep(5)

# the next tall thin rectangle needs to be drawn 5 pixels to the right of the last one
    i += 5 
