from gtts import gTTS
import os

def text_to_speech(text, lang, filename):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    os.system(f"mpg321 {filename}")

text = "hello im Ali Mallah"
lang = 'en'
filename = 'speech.mp3'
text_to_speech(text, lang, filename)
