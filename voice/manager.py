from core.router import router

from voice.listen import listener
from voice.speech import speech
from voice.wakeword import wakeword
from voice.conversation import conversation


class VoiceManager:

    def __init__(self):

        self.running = True

    def stop(self):

        self.running = False

    def run(self):

        print()
        print("=" * 50)
        print("NOVA Voice Engine Started")
        print("=" * 50)

        while self.running:

            text = listener.listen()

            if not self.running:
                break

            if not text:
                continue

            print(f"You : {text}")

            # -----------------------------
            # Sleeping
            # -----------------------------

            if not conversation.awake():

                if wakeword.detect(text):

                    conversation.wake()

                    print("Nova : Yes?")
                    speech.speak("Yes?")

                continue

            # -----------------------------
            # User is talking
            # -----------------------------

            conversation.touch()

            reply = router.process(text)

            if reply == "__EXIT__":

                speech.speak("Goodbye.")
                break

            if reply:

                print(f"Nova : {reply}")
                speech.speak(reply)

            # -----------------------------
            # Timeout
            # -----------------------------

            if conversation.sleeping():

                print("Nova : Going back to sleep.")
                speech.speak("Going back to sleep.")


voice_manager = VoiceManager()