from gtts import gTTS
import os

# متن فارسی
text = "سلام، چطوری؟"

# تبدیل متن به گفتار
speech = gTTS(text=text, lang='fa')

# ذخیره فایل صوتی
speech.save("output.mp3")

# پخش فایل صوتی
os.system("mpg321 output.mp3")
