from agents.base_agent import BaseAgent


class DefaultAgent(BaseAgent):
    def process(self, user_input: str) -> str:
        prompt = (
            f"{self.system_prompt}\n{user_input}" if self.system_prompt else user_input
        )
        return self.model.generate(prompt)

    def capabilities(self):
        return ["process"]
