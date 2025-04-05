# class BaseAgent:
#     def __init__(
#         self, name, model, description, system_prompt, tools=None, params=None
#     ):
#         self.name = name
#         self.model = model
#         self.description = description
#         self.system_prompt = system_prompt
#         self.tools = tools or []
#         self.params = params or {}
#
#     def respond(self, message):
#         """
#         에이전트가 메시지를 받아 응답하는 메서드
#         추상 메서드로, 실제 에이전트에서 오버라이드해야 함
#         """
#         raise NotImplementedError("respond() must be implemented by subclasses.")
#


class BaseAgent:
    def __init__(
        self, name, model, description, system_prompt, tools=None, params=None
    ):
        self.name = name
        self.model = model
        self.description = description
        self.system_prompt = system_prompt
        self.tools = tools or []
        self.params = params or {}

    def run(self, message):
        # 아직은 실제 LLM 호출 없이 그냥 프롬프트 확인용
        return f"[{self.name}] 프롬프트: {self.system_prompt}\n입력: {message}"
