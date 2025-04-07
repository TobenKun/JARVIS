from agents.agent_factory import AgentFactory
from agents.base_agent import BaseAgent


class AgentBroker:
    def __init__(self, config_path: str):
        self.factory = AgentFactory(config_path)
        self.agents: dict[str, BaseAgent] = self.factory.load_agents()

    def load_agents(self):
        """에이전트를 이름 기준으로 등록"""
        self.agents = self.factory.load_agents()

    def get_agent(self, name: str) -> BaseAgent | None:  # TODO: 커스텀 예외로 수정하기
        """이름으로 에이전트 검색"""

        # check = self.agents.get(name)
        # if check is None:
        #     raise ValueError(name + "에이전트가 존재하지 않습니다")

        return self.agents.get(name)

    def ask(self, user_input: str) -> str:
        """
        브로커 클래스의 진입점
        여기서 분석, 라우팅, 에러처리 하면 편할듯
        """
        return self.route_request(user_input)

    def route_request(self, user_input: str) -> str:
        """
        단순 키워드 기반 라우팅 로직 (임시 버전)
        추후에 WorkflowManager와 연결해서 더 지능적으로 변경 예정
        """
        # 예시: 키워드 기반 분기
        if "계산" in user_input:
            agent = self.get_agent("function_agent")
        elif "요약" in user_input:
            agent = self.get_agent("summarizer")
        else:
            agent = self.get_agent("researcher")

        if agent:
            return agent.process(user_input)
        else:
            return "요청을 처리할 수 있는 에이전트를 찾지 못했습니다."
