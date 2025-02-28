from deep_translator import GoogleTranslator

class GoogleTranslatorService:
    def translate(self, text, dest):
        translated_text = GoogleTranslator(source='auto', target=dest).translate(text)
        return type("Translation", (), {"text": translated_text})()
