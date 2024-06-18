import speech_recognition as sr

def whisper_transcriber(audio, api_key, type="path"):
    r = sr.Recognizer()

    if type=="path":
        with sr.AudioFile(audio) as source:
            audio = r.record(source)
    elif type=="microphone":
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout=2, phrase_time_limit=3)

    try:
        text = r.recognize_whisper_api(audio, api_key=api_key)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand audio"
    except sr.RequestError as e:
        return f"Error with the speech recognition service; {e}"
    except AssertionError:
        return "No audio to transcribe."