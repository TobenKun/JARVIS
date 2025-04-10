import os
from dotenv import load_dotenv
from core.conductor import Conductor
from core.work_flow import Workflow
from core.agent_broker import AgentBroker
from model.openrouter_adapter import OpenRouterAdapter
from agents.default_agent import DefaultAgent
from agents.agent_factory import AgentFactory
from utils.translation import translate_to_en


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

result = translate_to_en("지구의 최초 생명체에 대해 알려줘")
print(result)
exit(0)

# factory = AgentFactory("config/agents.yaml")
# agents = factory.load_agents()
#
# first_respond = agents["researcher"].process("쇼팽의 음악 세계에 대해 알려줘")
# print(first_respond)
# print("\n\n 요약중...\n\n")
# second_respond = agents["summarizer"].process(first_respond)
# print(second_respond)

broker = AgentBroker("config/agents.yaml")
#
# input = "사과 2개 더하기 사과 3개는 몇개인지 계산해줘"
# output = broker.ask(input)
# print(output)

conductor = Conductor(broker)
result = conductor.handle("인류의 발전 과정에 대해 조사하고 요약해줘")
print(result)
