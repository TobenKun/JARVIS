# default_agent.py
class DefaultAgent:
    def __init__(self, system_prompt=None):
        self.system_prompt = system_prompt or "You are a helpful assistant."

    def process(self, user_input: str) -> str:
        prompt = f"{self.system_prompt}\n{user_input}"
        return f"[DefaultAgent]: {prompt}"  # 실제로는 model.generate() 사용

    def capabilities(self):
        return ["process"]
