from intent.classifier import classifier


class IntentEngine:

    def detect(self, text):

        return classifier.classify(text)


intent_engine = IntentEngine()