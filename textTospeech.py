import pyttsx3



def speak(text,userRate,userVolume,voiceIndex):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate',userRate)
    engine.setProperty('volume', userVolume)

    fones = engine.getProperty('voices')
    if 0 <= voiceIndex <= len(fones):
        engine.setProperty('voice', fones[voiceIndex].id)

    engine.say(text)
    engine.runAndWait()
engineTemp = pyttsx3.init()
fones = engineTemp.getProperty('voices')

print('Available voices:')
for i,v in enumerate(fones):
    print(i,  '-' , v.name)
userText = input("what do you want me to say? ")
userRate = int(input("Choose the rate of the text -100 - 100"))
userVolume = float(input("Choose the volume of the text from 0.1 - 0.9"))
voiceChoice = int(input("Choose the voice of the text from 0 to 5"))



if userRate >100 or userRate <100:
    print("False input")

elif userVolume <0.1 or userVolume >0.9:
    print("False input")


speak(userText,userRate,userVolume,voiceChoice)


