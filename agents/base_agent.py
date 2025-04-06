from abc import ABC, abstractmethod
from model.base_model import BaseModel


class BaseAgent(ABC):
    def __init__(self, name: str, model: BaseModel, system_prompt: str = ""):
        self.name = name
        self.model = model
        self.system_prompt = system_prompt

    @abstractmethod
    def process(self, user_input: str) -> str:
        """에이전트가 유저 입력을 처리하는 메서드"""
        pass

    @abstractmethod
    def capabilities(self):
        """에이전트가 지원하는 기능 목록"""
        pass
