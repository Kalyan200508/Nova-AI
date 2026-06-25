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

        # Use Windows default microphone
        self.device = None

        print("Using microphone:")
        print(sd.query_devices(kind="input")["name"])

        print("Whisper loaded.")

    def listen(self, duration=4, sample_rate=16000):

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
                language="en",
                beam_size=5,
                vad_filter=True,
                temperature=0.0
            )

            text = " ".join(segment.text for segment in segments).strip()

            print("=" * 60)
            print("Language    :", info.language)
            print("Probability :", info.language_probability)
            print("Text        :", repr(text))
            print("=" * 60)

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