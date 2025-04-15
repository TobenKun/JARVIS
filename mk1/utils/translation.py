import deepl

#TODO: should i make translator adaptor?

# def translate_to_en(input: str) -> str:
#     api_key = os.getenv("DEEPL_API_KEY")
#     translator = deepl.Translator(api_key)
#
#     result = translator.translate_text(input, target_lang="EN-US")
#     return result.text

class Translator:
    def __init__(self, api_key: str):
        self.translator = deepl.Translator(api_key)

    def to_english(self, text: str) -> str:
        return self.translator.translate_text(text, target_lang="EN-US").text

    def to_korean(self, text: str) -> str:
        return self.translator.translate_text(text, target_lang="KO").text
