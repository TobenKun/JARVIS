from langchain_community.chat_models import ChatOpenAI
from typing import Optional
import os

class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(self,
                 model_name: str,
                 openai_api_key: Optional[str] = None,
                 openai_api_base: str = "https://openrouter.ai/api/v1",
                 **kwargs):
        openai_api_key = openai_api_key or os.getenv('OPENROUTER_API_KEY')
        super().__init__(openai_api_base=openai_api_base,
                         openai_api_key=openai_api_key,
                         model_name=model_name, **kwargs)


def test():
    from dotenv import load_dotenv
    from langchain_core.prompts import ChatPromptTemplate

    load_dotenv()
    llm = ChatOpenRouter(
        model_name="meta-llama/llama-4-maverick:free"
    )
    prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
    openrouter_chain = prompt | llm
    print(openrouter_chain.invoke({"topic": "banana"}))

if __name__ == "__main__":
    test()
