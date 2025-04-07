import os
from dotenv import load_dotenv
from core.work_flow import Workflow
from core.agent_broker import AgentBroker
from model.openrouter_adapter import OpenRouterAdapter
from agents.default_agent import DefaultAgent
from agents.agent_factory import AgentFactory


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

broker = AgentBroker("config/agents.yaml")
#
# input = "사과 2개 더하기 사과 3개는 몇개인지 계산해줘"
# output = broker.ask(input)
# print(output)

workflow = Workflow(
    steps=[
        broker.get_agent("researcher"),
        broker.get_agent("summarizer"),
    ],
    input_data="샴 고양이에 대해 알려줘",
)

output = workflow.run()
print(output)
