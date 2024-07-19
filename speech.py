import pyttsx3
engine=pyttsx3.init()
# engine.say("here is the piece of code")
# engine.runAndWait()
engine.save_to_file("this is the speech i am saying","./speech_spoken.mp4")
engine.runAndWait()