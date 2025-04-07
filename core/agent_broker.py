from agents.agent_factory import AgentFactory
from agents.base_agent import BaseAgent

"""
에이전트의 목록을 관리하는 클래스
판단이나 실행은 하지 않음
"""


class AgentBroker:
    def __init__(self, config_path: str):
        self.factory = AgentFactory(config_path)
        self.agents: dict[str, BaseAgent] = self.factory.load_agents()

    def reload_agents(self):
        """에이전트 목록 전체를 리로드"""
        self.agents = self.factory.load_agents()

    def get_agent(self, name: str) -> BaseAgent | None:
        # TODO: 커스텀 예외로 수정하기
        """이름으로 에이전트 검색"""
        return self.agents.get(name)

    def has_agent(self, name: str) -> bool:
        """해당 이름의 에이전트가 존재하는지 확인"""
        return name in self.agents

    def list_agents(self) -> list[str]:
        """등록된 에이전트 목록 반환"""
        return list(self.agents.keys())

