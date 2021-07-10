import pyttsx3

file = open('./txt.txt', 'r', encoding='utf8')
texto = file.read()

speaker = pyttsx3.init()

voices = speaker.getProperty('voices')

for voice in voices:
    if voice == 'brazil':
        speaker.setProperty('voice', voice.id)

rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate+20)

print(texto)
speaker.say(texto)
speaker.runAndWait()
