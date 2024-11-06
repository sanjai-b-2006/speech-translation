import speech_recognition as sr 
from translate import Translator
import os
import gtts as gt
r= sr.Recognizer()
with sr.Microphone() as source:
    print ("Say Something in Tamil and pause")
    audio = r.listen (source)    
    print ("Got you")
try:
    WUS = r.recognize_google (audio, language="hi-IN")
    print('Recognized Audio')
    print (WUS)
    mc=open("utube.txt",'a+',encoding="utf-8")
    mc.writelines(WUS)
    mc.close()
    language='en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("utube.mp3")
    os.system("utube1234.mp3")
except:
    pass



        

    
            
   





