from core.router import router
from voice.conversation import conversation
from voice.listener import listener
from voice.speech import speech
from voice.wakeword import wakeword


class VoiceManager:

    def run(self):

        print()
        print("========== NOVA VOICE ==========")
        print()

        while True:

            text = listener.listen()

            if not text:
                continue

            print(f"You: {text}")

            # Sleeping mode
            if not conversation.awake():

                if wakeword.detect(text):

                    speech.speak("Yes?")

                    conversation.wake()

                continue

            # Keep conversation alive
            conversation.touch()

            reply = router.process(text)

            if reply == "__EXIT__":

                speech.speak("Goodbye.")

                break

            if reply:

                print(f"Nova: {reply}")

                speech.speak(reply)

            if conversation.sleeping():

                speech.speak("Going back to sleep.")


voice_manager = VoiceManager()