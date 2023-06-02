import streamlit as stl
import speech_recognition as spr

def transcribe_audio():
    rd = spr.Recognizer()
    with spr.Microphone() as source:
        stl.info("Listening... Please speak into the microphone.")
        audio = rd.listen(source)

    try:
        stl.info("Transcribing...")
        text = rd.recognize_google(audio)
        stl.success("Transcription: {}".format(text))
    except spr.UnknownValueError:
        stl.error("Unable to transcribe audio.")
    except spr.RequestError as e:
        stl.error("Error during transcription: {}".format(str(e)))

def main():
    stl.title("Real-time Voice Transcription BY GAUTAM MEHTO")
    stl.write("Speak into your microphone and see the transcription below:")

    if stl.button("Start Transcription"):
        transcribe_audio()

if __name__ == "__main__":
    main()
