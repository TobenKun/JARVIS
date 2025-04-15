import os
from dotenv import load_dotenv
from core.conductor import Conductor
from core.work_flow import Workflow
from core.agent_broker import AgentBroker
from model.openrouter_adapter import OpenRouterAdapter
from agents.default_agent import DefaultAgent
from agents.agent_factory import AgentFactory
from utils.translation import Translator


# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
#
# api_key = os.getenv("OPENROUTER_API_KEY")
# if api_key is None:
#     raise ValueError("환경변수가 설정되지 않았습니다.")
# model = OpenRouterAdapter(
#     api_key, model="mistralai/mistral-small-3.1-24b-instruct:free"
# )
#
# agent = DefaultAgent(
#     name="assistant1", model=model, system_prompt="You are a helpful assistant."
# )
# response = agent.process("What's the best way to learn Python?")
# print("🧠 에이전트 응답:", response)
#

load_dotenv()

# factory = AgentFactory("config/agents.yaml")
# agents = factory.load_agents()
#
# first_respond = agents["researcher"].process("쇼팽의 음악 세계에 대해 알려줘")
# print(first_respond)
# print("\n\n 요약중...\n\n")
# second_respond = agents["summarizer"].process(first_respond)
# print(second_respond)

config_path = "config/agents.yaml"
deepl_api_key = os.getenv("DEEPL_API_KEY")

translator = Translator(deepl_api_key)
broker = AgentBroker()
conductor = Conductor(broker, translator)

result = conductor.handle("세계2차대전에대해 설명해줘")
print(result)
