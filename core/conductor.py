from core.work_flow import Workflow
from core.agent_broker import AgentBroker
from utils.translation import Translator


# TODO: LLM 기반 판단 로직 도입
#       워크플로우 실행 전에 유저 인풋 전처리
#       실패한 스텝 처리
class Conductor:
    def __init__(self, broker: AgentBroker, translator: Translator):
        self.broker = broker
        self.translator = translator

    def compose_workflow(self, user_input: str) -> Workflow:
        """
        user_input을 분석해서 어떤 agent들이 필요한지 판단한 뒤,
        워크플로우를 구성해서 반환
        """
        steps = []

        # 🔧 단순 키워드 기반 분기 (향후 LLM 기반 판단으로 교체 가능)
        if "research" in user_input or "Research" in user_input:
            steps.append(self.broker.get_agent("researcher"))
        if "summarize" in user_input:
            steps.append(self.broker.get_agent("summarizer"))
        if not steps:
            steps.append(self.broker.get_agent("default_agent"))

        return Workflow(steps, input_data=user_input)

    def handle(self, user_input: str) -> str:
        """
        전체 입출력 흐름의 진입점
        입력당 하나의 워크플로우를 만들고 실행
        """
        english_input = self.translator.to_english(user_input);
        print("## TRANSLATED INPUT: " + english_input)
        workflow = self.compose_workflow(english_input)
        result = workflow.run()
        print()
        print("## BEFORE TRANSLATE: " + result)
        return self.translator.to_korean(result)
