import pyttsx3
def text_to_speech(text):
   try:
     engine=pyttsx3.init()
     engine.setProperty('rate',150)
     engine.say(text)
     engine.runAndWait()
   except Exception as e:
      System.out.println("error",e)
#choice = input("Choose voice (male/female): ")
if __name__ =="main":
 text_to_speech("hello  this is Aiza your Voice Assistant")
#voices=engine.getProperty('voices')
    #if(gender.lower()=="male"):
    #engine.setProperty('voice',voices[0].id)
    #else:
    #engine.setProperty('voice',voices[1].id)

