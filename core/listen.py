import os
import tempfile
import wave

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel


class Listener:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        # Use your laptop's built-in microphone
        self.device = 1

        print("Whisper loaded.")

    def listen(self, duration=5, sample_rate=16000):

        print("\nListening... Speak now.")

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.int16,
            device=self.device
        )

        sd.wait()

        print("Recording finished.")

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        temp_name = temp.name
        temp.close()

        with wave.open(temp_name, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(recording.tobytes())

        try:

            segments, info = self.model.transcribe(
                temp_name,
                beam_size=1,
                vad_filter=False,
                language=None
            )

            text = ""

            for segment in segments:
                text += segment.text + " "

            text = text.strip()

            print("=" * 50)
            print("Detected Language :", info.language)
            print("Confidence        :", info.language_probability)
            print("Recognized Text   :", repr(text))
            print("=" * 50)

            if text == "":
                return ""

            return text

        except Exception as e:

            print("Whisper Error:", e)

            return ""

        finally:

            try:
                os.remove(temp_name)
            except Exception:
                pass


listener = Listener()