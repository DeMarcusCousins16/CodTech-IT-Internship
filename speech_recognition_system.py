import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

if __name__ == "__main__":
    audio_file = "sample.wav"  # Replace with your audio file
    transcription = transcribe_audio(audio_file)
    print("Transcription:\n", transcription)