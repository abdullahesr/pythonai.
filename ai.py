import speech_recognition as sr
from gtts import gTTS
import os
#abdullah_esr

recognizer = sr.Recognizer()

assistant_speech = "Merhaba, size nasıl yardımcı olabilirim?"


while True:
    try:
        with sr.Microphone() as source:
            print("Dinliyorum...")
            recognizer.adjust_for_ambient_noise(source) 
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="tr-TR")
            print(f"Komut: {command}")

            if "selam" in command.lower():
                response = assistant_speech
            elif "saat kaç" in command.lower():#soru ekleme bloğu
                import datetime
                now = datetime.datetime.now()
                response = f"Şu an saat {now.hour}:{now.minute}."
            elif "teşekkürler" in command.lower():
                response = "Rica ederim, size nasıl daha fazla yardımcı olabilirim?"
            elif "güle güle" in command.lower():
                response = "Güle güle, iyi günler dilerim!"
                break 

            
            tts = gTTS(response, lang="tr")
            tts.save("response.mp3")
            os.system("vlc response.mp3") 

    except sr.UnknownValueError:
        print("Anlaşılmayan komut.")
    except sr.RequestError as e:
        print(f"Hata oluştu: {str(e)}")
