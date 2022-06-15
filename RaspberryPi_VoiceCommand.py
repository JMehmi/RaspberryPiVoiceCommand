import speech_recognition as sr
import serial
import pytz
import time
import re
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)

import os
r= sr.Recognizer()
led=27
text = {}
text1 = {}
GPIO.setwarnings(False)


def listen1():
    with sr.Microphone(device_index = 2) as source:
               r.adjust_for_ambient_noise(source)
               print("Say Something");
               audio = r.listen(source)
               print("got it");
    return audio

def voice(audio1):
       try: 
         text1 = r.recognize_google(audio1) 
         print ("you said: " + text1);
         return text1; 
       except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand") 
#         return 0
       except sr.RequestError as e: 
        print("Could not request results from Google")
#         return 0

def main(text):
       
       audio1 = listen1() 
       text = voice(audio1);
       text = {}
       
if __name__ == '__main__':
 while(1):
     audio1 = listen1() 
     text = voice(audio1)


     if 'light on' in text:
          GPIO.output(32,GPIO.LOW)
          print ("Lights on")
     elif 'light off' in text:
          GPIO.output(32,GPIO.HIGH)
          print ("Lights Off")  
     else:
           print("Please repeat")

     if 'turn on after ' in text:
       numeric_in=re.findall('[0-9]+',text)
       seconds=int(numeric_in[0])
       print("Light will be turned on in: ",seconds,"seconds")
       while seconds:
         mins,secs= divmod(seconds, 60)#the timer will be in seconds so it does automatically the mod by 60
         timer='{:02d}:{:02d}'.format(mins,secs)
         print(timer)
         time.sleep(1)
         seconds-=1

       GPIO.output(32,GPIO.LOW)
       print ("Lights on") 
      
     elif 'turn off after' in text:
       numeric_in=re.findall('[0-9]+',text)
       seconds=int(numeric_in[0])
       print("Light will be turned off in: ",seconds,"seconds")
       while seconds:
          mins,secs= divmod(seconds, 60)#the timer will be in seconds so it does automatically the mod by 60
          timer='{:02d}:{:02d}'.format(mins,secs)
          print(timer)
          time.sleep(1)
          seconds-=1
       GPIO.output(32,GPIO.HIGH)
       print ("Lights off") 



      

         
        

