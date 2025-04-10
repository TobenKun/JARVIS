import deepl
import os


def translate_to_en(input: str) -> str:
    api_key = os.getenv("DEEPL_API_KEY")
    translator = deepl.Translator(api_key)

    result = translator.translate_text(input, target_lang="EN-US")
    return result.text
