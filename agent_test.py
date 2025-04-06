import os
from dotenv import load_dotenv
from model.openrouter_adapter import OpenRouterAdapter
from agents.default_agent import DefaultAgent

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

api_key = os.getenv("OPENROUTER_API_KEY")
model = OpenRouterAdapter(
    api_key, model="mistralai/mistral-small-3.1-24b-instruct:free"
)

agent = DefaultAgent(
    name="assistant1", model=model, system_prompt="You are a helpful assistant."
)
response = agent.process("What's the best way to learn Python?")
print("🧠 에이전트 응답:", response)
