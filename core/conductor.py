from core.work_flow import Workflow
from core.agent_broker import AgentBroker


class Conductor:
    def __init__(self, broker: AgentBroker):
        self.broker = broker

    def compose_workflow(self, user_input: str) -> Workflow:
        """
        user_input을 분석해서 어떤 agent들이 필요한지 판단한 뒤,
        워크플로우를 구성해서 반환
        """
        steps = []

        # 🔧 단순 키워드 기반 분기 (향후 LLM 기반 판단으로 교체 가능)
        if "조사" in user_input or "검색" in user_input:
            steps.append(self.broker.get_agent("researcher"))
        if "요약" in user_input:
            steps.append(self.broker.get_agent("summarizer"))
        if not steps:
            steps.append(self.broker.get_agent("default_agent"))

        return Workflow(steps, input_data=user_input)

    def handle(self, user_input: str) -> str:
        """
        전체 입출력 흐름의 진입점
        입력당 하나의 워크플로우를 만들고 실행
        """
        workflow = self.compose_workflow(user_input)
        return workflow.run()
