# from gpiozero import LED
# 
# led=LED(25)
# 
# led.on()
# led.off()

#from gpiozero import LED
#from time import sleep
#
#led=LED(25)
# 
#for i in range(0,5):
#    led.on()
#    sleep(1)
#    led.off()
#    sleep(1)


#from gpiozero import LED
#from time import sleep
#led=LED(25)
 
#for i in range(0,3):
    #led.on()
    #sleep(.5)
    #led.off()
   # sleep(.5)
#for i in range(0,3):
    #led.on()
    #sleep(1)
    #led.off()
    #sleep(1)
     
#for i in range(0,3):
    #led.on()
    #sleep(.5)
    #led.off()
    #sleep(.5)


#from gpiozero import LED
#from time import sleep

#led1=LED(2)
#led2=LED(3)
#led3=LED(4)
#led4=
#led5=
#led6=
#led7=

#for i in range(0,3):
#    led1.on()
#    sleep(1)
#    led1.off()
#    sleep(1)
#    led2.on()
#    sleep(1)
#    led2.off()
#    sleep(1)
#    led3.on()
#    sleep(1)
#    led3.off()
#    sleep(1)
 #   led4.on()
  #  sleep(1)
   # led4.off()
    #sleep(1)
 #   led5.on()
  #  sleep(1)
   # led5.off()
    #sleep(1)
 #   led6.on()
  #  sleep(1)
   # led6.off()
    #sleep(1)
#    led7.on()
 #   sleep(1)
  #  led7.off()
   # sleep(1)
 
eighth=0.5
quarter=1
half=2
 
notes=["c","c","d","c","f","e","c","c","d","c","g","f","c","c","c","a","f","e","d","b","b","a","f","g","f"]
times=[eighth,eighth,quarter,quarter,quarter,half,eighth,eighth,quarter,quarter,quarter,half,eighth,eighth,quarter,quarter,quarter,quarter,quarter,eighth,eighth,quarter,quarter,quarter,half]

from gpiozero import LED
from time import sleep

ledA=LED(2)
ledB=LED(3)
ledC=LED(4)
ledD=LED(17)
ledE=LED(27)
ledF=LED(22)
ledG=LED(10)

for i in range(len(notes)):
    if notes[i] == "a":
        ledA.on()
        sleep(times[i])
        ledA.off()
    if notes[i] == "b":
        ledB.on()
        sleep(times[i])
        ledB.off()
    if notes[i] == "c":
        ledC.on()
        sleep(times[i])
        ledC.off()
    if notes[i] == "d":
        ledD.on()
        sleep(times[i])
        ledD.off()
    if notes[i] == "e":
        ledE.on()
        sleep(times[i])
        ledE.off()
    if notes[i] == "f":
        ledF.on()
        sleep(times[i])
        ledF.off()
    if notes[i] == "g":
        ledG.on()
        sleep(times[i])
        ledG.off()
    
        
#for i in range(0,8):
    