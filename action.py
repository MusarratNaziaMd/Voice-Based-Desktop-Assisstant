import speech_to_text
import text_to_speech
import datetime
import webbrowser
def Action(data):
    print("DEBUG (user_data):", data)
    user_data=data.lower()#converting into lower cases

    if"what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Aiza - Your Voice assistant")
        return "My name is Aiza - Your Voice Assistant"
    elif "hello" in user_data or "hi" in user_data:
        response = "Hello, how may I help you?"
        print("DEBUG: responding with →", response)
        text_to_speech.text_to_speech(response)
        return  response
    elif "good morning"in user_data:
        text_to_speech.text_to_speech("Good Morning")
        return "Good Morning"
    elif "good afternoon"in user_data:
        text_to_speech.text_to_speech("Good Afternoon")
        return "good Aternoon"
    elif "good evening"in user_data:
        text_to_speech.text_to_speech("Good Evening")
        return "good evening"
    elif "time now" in user_data:
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+" Hour:",(str)(current_time.minute)+ "Minute"
        text_to_speech.text_to_speech("%I%M%S"+Time)
        return "Time"
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok ")
        return "ok"
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/album/1ZrWlhMUoyMKsoQ1tvRR2t?highlight=spotify:track:4Q0qVhFQa7j6jRKzo3HDmP/")
        text_to_speech.text_to_speech("Spotify is ready Enjoy your music")
        return "Spotify is ready"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("Youtube is ready.....Enjoy")
        return"Youtube is ready"
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google is ready")
        return "Google"
    else:
        text_to_speech.text_to_speech("Sorry!Unable to understand")
    return"Sorry!Unable to hear"
        





