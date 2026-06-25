import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import tempfile
import wave
import os


class Listener:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper loaded.")

    def listen(self, duration=5, sample_rate=16000):

        print("Listening...")

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.int16
        )

        sd.wait()

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

        segments, info = self.model.transcribe(
            temp_name,
            language="en",
            beam_size=5,
            vad_filter=True,
            condition_on_previous_text=False
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        text = text.strip()

        try:
            os.remove(temp_name)
        except:
            pass

        return text


listener = Listener()