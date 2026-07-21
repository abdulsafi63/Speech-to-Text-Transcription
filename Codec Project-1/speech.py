import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import numpy as np

class SpeechToText:

    def __init__(self):
        self.sample_rate = 44100
        self.channels = 1
        self.duration = 10

    def record_audio(self):

        try:

            print("Recording...")

            recording = sd.rec(
                int(self.duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype="float32"
            )

            sd.wait()

            sf.write("recorded.wav", recording, self.sample_rate)

            recognizer = sr.Recognizer()

            with sr.AudioFile("recorded.wav") as source:
                audio = recognizer.record(source)

            text = recognizer.recognize_google(audio)

            with open("output.txt", "w", encoding="utf-8") as f:
                f.write(text)

            return text

        except sr.UnknownValueError:
            return "Could not understand speech."

        except sr.RequestError:
            return "Internet connection required."

        except Exception as e:
            return str(e)